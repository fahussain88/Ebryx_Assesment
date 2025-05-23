{{- /*
Return the fullname for resources
Replaces underscores with dashes to conform to DNS-1123
*/ -}}
{{- define "py-app-helm-chart.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride | replace "_" "-" -}}
{{- printf "%s-%s" $name .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
