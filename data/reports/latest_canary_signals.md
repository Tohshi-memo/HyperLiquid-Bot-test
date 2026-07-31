# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T20:37:31.445107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0414` n `230`; crypto_major avg `0.0132` n `8`; equity avg `-0.0215` n `102`; fx avg `-0.0237` n `6`; index avg `0.0248` n `25`; metal avg `0.014` n `20`; unknown avg `2.3056` n `780`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.1405` n `230`; crypto_major avg `0.0608` n `8`; equity avg `-0.4411` n `102`; fx avg `-0.0927` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0222` n `20`; unknown avg `-0.0846` n `780`
- 4h: commodity avg `0.1556` n `12`; crypto_alt avg `0.1363` n `230`; crypto_major avg `-0.1101` n `8`; equity avg `-0.2476` n `102`; fx avg `-0.0121` n `6`; index avg `0.0095` n `25`; metal avg `0.0879` n `20`; unknown avg `7.2094` n `780`
- 24h: commodity avg `0.1665` n `12`; crypto_alt avg `-0.5025` n `230`; crypto_major avg `-1.9514` n `8`; equity avg `-0.789` n `102`; fx avg `0.1219` n `6`; index avg `0.1417` n `25`; metal avg `-0.3602` n `20`; unknown avg `0.2485` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
