# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T02:45:20.969710+00:00`
- Correlation status: `ready`
- Asset price records: `130`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `7`; crypto_alt avg `0.1091` n `223`; crypto_major avg `0.0531` n `7`; equity avg `0.0012` n `42`; fx avg `0.0` n `4`; index avg `0.0003` n `9`; metal avg `0.0019` n `7`; unknown avg `0.0475` n `313`
- 1h: commodity avg `-0.0254` n `7`; crypto_alt avg `-0.2072` n `223`; crypto_major avg `-0.1419` n `7`; equity avg `-0.0629` n `42`; fx avg `0.0029` n `4`; index avg `-0.0279` n `9`; metal avg `0.0103` n `7`; unknown avg `0.1109` n `313`
- 4h: commodity avg `0.0346` n `7`; crypto_alt avg `-1.2311` n `223`; crypto_major avg `-0.8339` n `7`; equity avg `-0.0277` n `42`; fx avg `0.0064` n `4`; index avg `-0.0229` n `9`; metal avg `-0.0008` n `7`; unknown avg `-0.0844` n `313`
- 24h: commodity avg `-0.1597` n `7`; crypto_alt avg `0.6724` n `223`; crypto_major avg `-0.3781` n `7`; equity avg `0.5266` n `42`; fx avg `0.0062` n `4`; index avg `0.0138` n `9`; metal avg `0.0349` n `7`; unknown avg `0.1405` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4498`, n `126`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4346`, n `126`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4277`, n `126`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4173`, n `126`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4173`, n `126`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4143`, n `122`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4119`, n `122`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4048`, n `122`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `126`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3997`, n `122`, moderate_sample_signal
