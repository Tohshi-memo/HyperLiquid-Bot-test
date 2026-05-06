# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T07:00:35.575194+00:00`
- Correlation status: `ready`
- Asset price records: `432`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1338` n `7`; crypto_alt avg `0.0371` n `223`; crypto_major avg `0.0707` n `7`; equity avg `0.0097` n `47`; fx avg `0.0147` n `4`; index avg `-0.1097` n `6`; metal avg `0.0442` n `7`; unknown avg `0.0131` n `313`
- 1h: commodity avg `0.3838` n `7`; crypto_alt avg `0.2319` n `223`; crypto_major avg `0.149` n `7`; equity avg `-0.0833` n `47`; fx avg `0.007` n `4`; index avg `-0.1166` n `6`; metal avg `-0.0502` n `7`; unknown avg `0.3471` n `313`
- 4h: commodity avg `0.2404` n `7`; crypto_alt avg `0.2515` n `223`; crypto_major avg `0.2985` n `7`; equity avg `0.5614` n `47`; fx avg `-0.2048` n `4`; index avg `0.2317` n `6`; metal avg `0.3105` n `7`; unknown avg `0.6888` n `311`
- 24h: commodity avg `-1.3398` n `7`; crypto_alt avg `2.6838` n `223`; crypto_major avg `1.6581` n `7`; equity avg `2.5332` n `47`; fx avg `-0.3855` n `4`; index avg `1.9963` n `6`; metal avg `2.0116` n `7`; unknown avg `1.6969` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1806`, n `428`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1743`, n `428`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1281`, n `428`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.126`, n `428`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `428`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `428`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1014`, n `424`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `424`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `428`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `428`, weak_sample_signal
