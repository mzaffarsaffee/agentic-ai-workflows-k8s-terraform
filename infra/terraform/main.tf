terraform {
  required_version = ">= 1.0"
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "agentic" {
  metadata {
    name = "agentic-ai"
  }
}
