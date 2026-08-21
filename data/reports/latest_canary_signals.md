# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T09:22:30.302056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `-0.1045` n `230`; crypto_major avg `0.172` n `8`; equity avg `0.0578` n `121`; fx avg `0.026` n `6`; index avg `-0.008` n `25`; metal avg `-0.0142` n `20`; unknown avg `-0.0469` n `793`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.6609` n `230`; crypto_major avg `-0.0761` n `8`; equity avg `0.3054` n `121`; fx avg `0.0258` n `6`; index avg `0.0235` n `25`; metal avg `0.071` n `20`; unknown avg `0.1464` n `793`
- 4h: commodity avg `0.0812` n `12`; crypto_alt avg `1.7137` n `230`; crypto_major avg `1.4809` n `8`; equity avg `0.4259` n `121`; fx avg `0.0143` n `6`; index avg `-0.0032` n `25`; metal avg `0.3759` n `20`; unknown avg `0.1582` n `777`
- 24h: commodity avg `0.0296` n `12`; crypto_alt avg `5.539` n `230`; crypto_major avg `5.719` n `8`; equity avg `0.3187` n `121`; fx avg `-0.0642` n `6`; index avg `0.0039` n `25`; metal avg `0.9193` n `20`; unknown avg `2.3054` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
