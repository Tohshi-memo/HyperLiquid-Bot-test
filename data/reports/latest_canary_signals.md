# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T20:52:28.151086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `-0.1302` n `231`; crypto_major avg `-0.2376` n `8`; equity avg `-0.0179` n `122`; fx avg `-0.0034` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0899` n `794`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `0.326` n `231`; crypto_major avg `0.309` n `8`; equity avg `0.0204` n `122`; fx avg `-0.0013` n `6`; index avg `-0.008` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0855` n `794`
- 4h: commodity avg `-0.1353` n `12`; crypto_alt avg `-0.9276` n `231`; crypto_major avg `-0.8409` n `8`; equity avg `-0.3746` n `122`; fx avg `-0.0123` n `6`; index avg `-0.0422` n `25`; metal avg `-0.0394` n `20`; unknown avg `-0.5546` n `793`
- 24h: commodity avg `-0.2677` n `12`; crypto_alt avg `-1.3772` n `231`; crypto_major avg `-0.586` n `8`; equity avg `-2.8733` n `122`; fx avg `-0.0671` n `6`; index avg `-0.3697` n `25`; metal avg `0.0759` n `20`; unknown avg `1.5535` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
