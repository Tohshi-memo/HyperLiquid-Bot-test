# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T06:20:59.113058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0282` n `230`; crypto_major avg `0.0015` n `8`; equity avg `0.0462` n `121`; fx avg `0.0013` n `6`; index avg `0.0095` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.0712` n `793`
- 1h: commodity avg `0.0233` n `12`; crypto_alt avg `0.6684` n `230`; crypto_major avg `0.4165` n `8`; equity avg `-0.0754` n `121`; fx avg `0.0375` n `6`; index avg `-0.0143` n `25`; metal avg `0.0964` n `20`; unknown avg `-0.0552` n `777`
- 4h: commodity avg `-0.1022` n `12`; crypto_alt avg `1.1734` n `230`; crypto_major avg `0.9176` n `8`; equity avg `-0.1042` n `121`; fx avg `0.0525` n `6`; index avg `0.0027` n `25`; metal avg `0.1247` n `20`; unknown avg `-0.0205` n `777`
- 24h: commodity avg `0.2678` n `12`; crypto_alt avg `6.4422` n `230`; crypto_major avg `7.4176` n `8`; equity avg `-0.4883` n `121`; fx avg `0.0321` n `6`; index avg `-0.0931` n `25`; metal avg `0.5665` n `20`; unknown avg `2.5855` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
