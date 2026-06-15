# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T20:37:40.139727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1263` n `12`; crypto_alt avg `-0.123` n `228`; crypto_major avg `-0.0361` n `8`; equity avg `0.0185` n `77`; fx avg `-0.0056` n `6`; index avg `0.0255` n `23`; metal avg `-0.0889` n `18`; unknown avg `0.1276` n `687`
- 1h: commodity avg `-0.0727` n `12`; crypto_alt avg `0.1477` n `228`; crypto_major avg `-0.0065` n `8`; equity avg `0.1478` n `77`; fx avg `-0.0137` n `6`; index avg `0.0291` n `23`; metal avg `-0.1446` n `18`; unknown avg `0.0489` n `687`
- 4h: commodity avg `0.5094` n `12`; crypto_alt avg `-1.4474` n `228`; crypto_major avg `-0.9223` n `8`; equity avg `-0.0792` n `77`; fx avg `-0.0537` n `6`; index avg `-0.1195` n `23`; metal avg `-0.42` n `18`; unknown avg `1.5392` n `687`
- 24h: commodity avg `-0.3373` n `12`; crypto_alt avg `4.4327` n `228`; crypto_major avg `6.35` n `8`; equity avg `2.9888` n `76`; fx avg `0.0035` n `6`; index avg `1.2781` n `23`; metal avg `1.8736` n `18`; unknown avg `5.4663` n `527`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
