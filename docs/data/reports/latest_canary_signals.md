# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T01:30:24.835243+00:00`
- Correlation status: `ready`
- Asset price records: `221`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0487` n `7`; crypto_alt avg `0.1152` n `223`; crypto_major avg `0.3844` n `7`; equity avg `0.0208` n `42`; fx avg `-0.0037` n `4`; index avg `0.0844` n `9`; metal avg `-0.1253` n `7`; unknown avg `-0.0197` n `314`
- 1h: commodity avg `-0.0802` n `7`; crypto_alt avg `0.6534` n `223`; crypto_major avg `0.7065` n `7`; equity avg `0.301` n `42`; fx avg `0.0037` n `4`; index avg `0.1371` n `9`; metal avg `-0.2232` n `7`; unknown avg `0.1559` n `314`
- 4h: commodity avg `0.6014` n `7`; crypto_alt avg `-0.0602` n `223`; crypto_major avg `0.13` n `7`; equity avg `0.0354` n `42`; fx avg `-0.004` n `4`; index avg `0.1953` n `9`; metal avg `-0.7161` n `7`; unknown avg `0.2191` n `314`
- 24h: commodity avg `0.0652` n `7`; crypto_alt avg `0.3659` n `223`; crypto_major avg `0.7417` n `7`; equity avg `0.3479` n `42`; fx avg `-0.0159` n `4`; index avg `0.2914` n `9`; metal avg `-0.1059` n `7`; unknown avg `0.3638` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3812`, n `217`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3655`, n `217`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3281`, n `213`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3276`, n `213`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2808`, n `217`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2707`, n `217`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2291`, n `217`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2096`, n `217`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.204`, n `213`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1998`, n `213`, weak_sample_signal
