# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T08:04:58.949585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0485` n `12`; crypto_alt avg `0.1815` n `230`; crypto_major avg `0.3292` n `8`; equity avg `0.0951` n `121`; fx avg `-0.0123` n `6`; index avg `0.0108` n `25`; metal avg `-0.0095` n `20`; unknown avg `0.0502` n `793`
- 1h: commodity avg `0.1177` n `12`; crypto_alt avg `1.2411` n `230`; crypto_major avg `0.5949` n `8`; equity avg `0.2257` n `121`; fx avg `-0.0524` n `6`; index avg `0.0366` n `25`; metal avg `0.0712` n `20`; unknown avg `0.1099` n `793`
- 4h: commodity avg `0.1207` n `12`; crypto_alt avg `2.5068` n `230`; crypto_major avg `1.5254` n `8`; equity avg `0.6625` n `121`; fx avg `-0.0114` n `6`; index avg `0.0803` n `25`; metal avg `0.1827` n `20`; unknown avg `0.099` n `777`
- 24h: commodity avg `0.352` n `12`; crypto_alt avg `7.2988` n `230`; crypto_major avg `7.2039` n `8`; equity avg `0.3185` n `121`; fx avg `-0.0683` n `6`; index avg `0.0159` n `25`; metal avg `0.7597` n `20`; unknown avg `2.4029` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
