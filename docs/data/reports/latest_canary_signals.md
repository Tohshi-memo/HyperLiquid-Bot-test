# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T14:15:52.946001+00:00`
- Correlation status: `ready`
- Asset price records: `367`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1569` n `7`; crypto_alt avg `-0.1619` n `223`; crypto_major avg `-0.1528` n `7`; equity avg `0.2991` n `47`; fx avg `0.004` n `4`; index avg `0.0775` n `6`; metal avg `-0.225` n `7`; unknown avg `0.4587` n `312`
- 1h: commodity avg `-0.1192` n `7`; crypto_alt avg `-0.4929` n `223`; crypto_major avg `-0.5628` n `7`; equity avg `-0.1388` n `47`; fx avg `-0.0006` n `4`; index avg `0.1899` n `6`; metal avg `-0.2128` n `7`; unknown avg `0.346` n `312`
- 4h: commodity avg `-0.5064` n `7`; crypto_alt avg `0.2624` n `223`; crypto_major avg `0.6826` n `7`; equity avg `0.4092` n `47`; fx avg `0.0446` n `4`; index avg `0.5488` n `6`; metal avg `0.1172` n `7`; unknown avg `0.6682` n `312`
- 24h: commodity avg `-0.0022` n `7`; crypto_alt avg `1.8015` n `223`; crypto_major avg `1.7505` n `7`; equity avg `0.0809` n `47`; fx avg `0.072` n `4`; index avg `0.4956` n `6`; metal avg `0.116` n `7`; unknown avg `0.5038` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2081`, n `363`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.201`, n `363`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `363`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `363`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `363`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `363`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `363`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `363`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0951`, n `359`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0898`, n `359`, weak_sample_signal
