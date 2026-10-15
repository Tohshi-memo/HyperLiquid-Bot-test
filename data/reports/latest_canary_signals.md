# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T10:37:29.870827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0361` n `13`; crypto_alt avg `0.2246` n `236`; crypto_major avg `0.1685` n `8`; equity avg `-0.0851` n `151`; fx avg `0.011` n `6`; index avg `0.0011` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0272` n `1112`
- 1h: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.3381` n `236`; crypto_major avg `-0.3317` n `8`; equity avg `-0.1079` n `151`; fx avg `-0.037` n `6`; index avg `-0.0004` n `26`; metal avg `-0.047` n `20`; unknown avg `-0.3225` n `1054`
- 4h: commodity avg `0.0162` n `13`; crypto_alt avg `0.1069` n `236`; crypto_major avg `0.0274` n `8`; equity avg `-0.3995` n `151`; fx avg `0.0196` n `6`; index avg `0.0165` n `26`; metal avg `0.2392` n `20`; unknown avg `4.3171` n `1038`
- 24h: commodity avg `-0.4823` n `13`; crypto_alt avg `-4.4653` n `236`; crypto_major avg `-3.3634` n `8`; equity avg `-5.963` n `151`; fx avg `0.0576` n `6`; index avg `-0.9435` n `26`; metal avg `-0.4074` n `20`; unknown avg `2.2831` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1224`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.087`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0869`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0804`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0687`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
