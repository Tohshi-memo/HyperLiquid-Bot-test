# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T20:45:23.744182+00:00`
- Correlation status: `ready`
- Asset price records: `391`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `7`; crypto_alt avg `0.1987` n `223`; crypto_major avg `0.1669` n `7`; equity avg `-0.0313` n `47`; fx avg `-0.0364` n `4`; index avg `-0.0212` n `6`; metal avg `-0.0789` n `7`; unknown avg `0.0349` n `313`
- 1h: commodity avg `0.0301` n `7`; crypto_alt avg `0.6377` n `223`; crypto_major avg `0.4068` n `7`; equity avg `0.3167` n `47`; fx avg `-0.0003` n `4`; index avg `0.0603` n `6`; metal avg `-0.0085` n `7`; unknown avg `-0.179` n `313`
- 4h: commodity avg `-0.0263` n `7`; crypto_alt avg `1.3266` n `223`; crypto_major avg `1.104` n `7`; equity avg `0.6452` n `47`; fx avg `0.0083` n `4`; index avg `0.2283` n `6`; metal avg `-0.2509` n `7`; unknown avg `0.1427` n `313`
- 24h: commodity avg `-1.0974` n `7`; crypto_alt avg `2.7698` n `223`; crypto_major avg `2.9201` n `7`; equity avg `2.346` n `47`; fx avg `-0.0524` n `4`; index avg `1.4034` n `6`; metal avg `0.6855` n `7`; unknown avg `1.1814` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `387`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2001`, n `387`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `387`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `387`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1135`, n `383`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `387`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `387`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `383`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.103`, n `387`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `387`, weak_sample_signal
