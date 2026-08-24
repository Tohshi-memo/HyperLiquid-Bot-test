# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T09:07:24.322297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.3531` n `231`; crypto_major avg `0.2855` n `8`; equity avg `0.0345` n `122`; fx avg `-0.0152` n `6`; index avg `0.0035` n `25`; metal avg `0.0117` n `20`; unknown avg `0.1181` n `793`
- 1h: commodity avg `-0.1039` n `12`; crypto_alt avg `-0.0732` n `231`; crypto_major avg `-0.1865` n `8`; equity avg `0.1935` n `122`; fx avg `-0.0248` n `6`; index avg `0.0447` n `25`; metal avg `-0.0504` n `20`; unknown avg `0.3381` n `793`
- 4h: commodity avg `0.0136` n `12`; crypto_alt avg `0.1127` n `231`; crypto_major avg `-0.0731` n `8`; equity avg `-0.1317` n `122`; fx avg `0.0251` n `6`; index avg `-0.0306` n `25`; metal avg `-0.0244` n `20`; unknown avg `0.2594` n `777`
- 24h: commodity avg `-0.2623` n `12`; crypto_alt avg `2.0162` n `231`; crypto_major avg `0.3867` n `8`; equity avg `-1.1682` n `122`; fx avg `-0.1434` n `6`; index avg `-0.0955` n `25`; metal avg `0.1234` n `20`; unknown avg `5.352` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
