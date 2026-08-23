# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T20:46:04.632042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.0014` n `231`; crypto_major avg `0.0061` n `8`; equity avg `0.0036` n `122`; fx avg `0.0055` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0377` n `793`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `-0.0424` n `231`; crypto_major avg `-0.0141` n `8`; equity avg `-0.0041` n `122`; fx avg `-0.0092` n `6`; index avg `-0.0091` n `25`; metal avg `0.0361` n `20`; unknown avg `1.1921` n `793`
- 4h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.1239` n `231`; crypto_major avg `0.0012` n `8`; equity avg `0.2056` n `122`; fx avg `-0.0746` n `6`; index avg `0.0422` n `25`; metal avg `0.0341` n `20`; unknown avg `1.802` n `793`
- 24h: commodity avg `-0.0752` n `12`; crypto_alt avg `2.1803` n `231`; crypto_major avg `0.0239` n `8`; equity avg `0.7473` n `122`; fx avg `-0.0709` n `6`; index avg `0.1258` n `25`; metal avg `0.1259` n `20`; unknown avg `5.5705` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
