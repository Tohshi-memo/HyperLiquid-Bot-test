# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T07:00:27.966015+00:00`
- Correlation status: `ready`
- Asset price records: `243`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `7`; crypto_alt avg `0.119` n `223`; crypto_major avg `0.0033` n `7`; equity avg `0.0061` n `42`; fx avg `-0.0016` n `4`; index avg `-0.0609` n `9`; metal avg `-0.0217` n `7`; unknown avg `-0.043` n `314`
- 1h: commodity avg `0.4945` n `7`; crypto_alt avg `-0.2489` n `223`; crypto_major avg `-0.5175` n `7`; equity avg `-0.1058` n `42`; fx avg `0.0159` n `4`; index avg `-0.0435` n `9`; metal avg `-0.3218` n `7`; unknown avg `-0.2043` n `314`
- 4h: commodity avg `0.2881` n `7`; crypto_alt avg `0.0` n `223`; crypto_major avg `-0.35` n `7`; equity avg `-0.4407` n `42`; fx avg `-0.0334` n `4`; index avg `0.1246` n `9`; metal avg `-0.6041` n `7`; unknown avg `-0.4037` n `312`
- 24h: commodity avg `0.4511` n `7`; crypto_alt avg `2.3261` n `223`; crypto_major avg `2.1865` n `7`; equity avg `1.0116` n `42`; fx avg `-0.0225` n `4`; index avg `0.8892` n `9`; metal avg `-0.3259` n `7`; unknown avg `-0.1448` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3981`, n `235`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3891`, n `235`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.356`, n `239`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3426`, n `239`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2112`, n `235`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1999`, n `235`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1782`, n `239`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1722`, n `239`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.171`, n `235`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1604`, n `239`, weak_sample_signal
