# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T22:07:36.470524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0461` n `13`; crypto_alt avg `0.1825` n `236`; crypto_major avg `0.122` n `8`; equity avg `0.1177` n `151`; fx avg `0.0094` n `6`; index avg `-0.0039` n `26`; metal avg `0.0111` n `20`; unknown avg `-0.0634` n `1118`
- 1h: commodity avg `0.0332` n `13`; crypto_alt avg `0.47` n `236`; crypto_major avg `0.3918` n `8`; equity avg `0.6158` n `151`; fx avg `0.0213` n `6`; index avg `0.0482` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2735` n `1118`
- 4h: commodity avg `-0.1926` n `13`; crypto_alt avg `0.3405` n `236`; crypto_major avg `0.3724` n `8`; equity avg `1.364` n `151`; fx avg `-0.0151` n `6`; index avg `0.1196` n `26`; metal avg `0.0921` n `20`; unknown avg `0.155` n `1036`
- 24h: commodity avg `-0.2358` n `13`; crypto_alt avg `0.7101` n `236`; crypto_major avg `0.9148` n `8`; equity avg `0.6483` n `151`; fx avg `0.2091` n `6`; index avg `-0.0339` n `26`; metal avg `0.5351` n `20`; unknown avg `23.7015` n `926`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0752`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0745`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0494`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.049`, n `666`, weak_sample_signal
