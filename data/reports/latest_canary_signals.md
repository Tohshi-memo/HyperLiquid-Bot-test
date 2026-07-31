# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T21:52:27.980310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0552` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `-0.0539` n `8`; equity avg `-0.0766` n `102`; fx avg `-0.0014` n `6`; index avg `-0.0196` n `25`; metal avg `0.0164` n `20`; unknown avg `1.9383` n `781`
- 1h: commodity avg `0.7375` n `12`; crypto_alt avg `-0.0917` n `230`; crypto_major avg `-0.0932` n `8`; equity avg `-0.3008` n `102`; fx avg `0.0113` n `6`; index avg `-0.0722` n `25`; metal avg `-0.0448` n `20`; unknown avg `-0.0246` n `781`
- 4h: commodity avg `0.8007` n `12`; crypto_alt avg `-0.6153` n `230`; crypto_major avg `-0.7001` n `8`; equity avg `-1.0604` n `102`; fx avg `-0.0123` n `6`; index avg `-0.1598` n `25`; metal avg `-0.0609` n `20`; unknown avg `-0.4279` n `780`
- 24h: commodity avg `0.9253` n `12`; crypto_alt avg `-0.6182` n `230`; crypto_major avg `-2.162` n `8`; equity avg `-1.4827` n `102`; fx avg `0.1157` n `6`; index avg `0.0207` n `25`; metal avg `-0.4303` n `20`; unknown avg `0.2103` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
