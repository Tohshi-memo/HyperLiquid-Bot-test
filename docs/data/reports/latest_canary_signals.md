# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T03:37:29.870044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.0883` n `228`; crypto_major avg `0.0458` n `8`; equity avg `-0.0196` n `88`; fx avg `0.0007` n `6`; index avg `-0.0171` n `23`; metal avg `0.0078` n `20`; unknown avg `11.5685` n `764`
- 1h: commodity avg `0.0432` n `12`; crypto_alt avg `-0.1138` n `228`; crypto_major avg `0.0244` n `8`; equity avg `0.0111` n `88`; fx avg `0.0055` n `6`; index avg `-0.0094` n `23`; metal avg `0.0097` n `20`; unknown avg `20.1369` n `764`
- 4h: commodity avg `0.0011` n `12`; crypto_alt avg `0.2419` n `228`; crypto_major avg `0.1553` n `8`; equity avg `0.1609` n `88`; fx avg `0.0209` n `6`; index avg `0.0185` n `23`; metal avg `0.0294` n `20`; unknown avg `0.1387` n `764`
- 24h: commodity avg `-0.0964` n `12`; crypto_alt avg `3.1283` n `228`; crypto_major avg `3.0726` n `8`; equity avg `2.4858` n `87`; fx avg `-0.025` n `6`; index avg `0.238` n `23`; metal avg `1.3497` n `20`; unknown avg `0.2752` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
