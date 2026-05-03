# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T19:40:01.409151+00:00`
- Correlation status: `ready`
- Asset price records: `197`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0464` n `7`; crypto_alt avg `0.0989` n `223`; crypto_major avg `0.1527` n `7`; equity avg `0.0397` n `42`; fx avg `0.0239` n `4`; index avg `0.0127` n `9`; metal avg `0.0158` n `7`; unknown avg `0.0378` n `314`
- 1h: commodity avg `-0.0432` n `7`; crypto_alt avg `0.1514` n `223`; crypto_major avg `0.1597` n `7`; equity avg `0.0906` n `42`; fx avg `0.0335` n `4`; index avg `0.0224` n `9`; metal avg `-0.0576` n `7`; unknown avg `0.0977` n `314`
- 4h: commodity avg `0.1991` n `7`; crypto_alt avg `0.2121` n `223`; crypto_major avg `0.165` n `7`; equity avg `0.3078` n `42`; fx avg `-0.0108` n `4`; index avg `0.0606` n `9`; metal avg `0.1966` n `7`; unknown avg `0.1` n `313`
- 24h: commodity avg `-0.0889` n `7`; crypto_alt avg `-0.1378` n `223`; crypto_major avg `0.1218` n `7`; equity avg `0.3805` n `42`; fx avg `0.0655` n `4`; index avg `0.061` n `9`; metal avg `0.4703` n `7`; unknown avg `0.1207` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.399`, n `193`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3812`, n `193`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3769`, n `189`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3751`, n `193`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3696`, n `189`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3618`, n `193`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3303`, n `193`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3116`, n `193`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3051`, n `193`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2529`, n `189`, moderate_sample_signal
