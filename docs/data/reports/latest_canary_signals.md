# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T14:52:26.507332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.2822` n `230`; crypto_major avg `0.1918` n `8`; equity avg `0.0953` n `121`; fx avg `0.0002` n `6`; index avg `0.0225` n `25`; metal avg `-0.0367` n `20`; unknown avg `-0.0188` n `793`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `0.4172` n `230`; crypto_major avg `0.0646` n `8`; equity avg `-0.5135` n `121`; fx avg `-0.0102` n `6`; index avg `-0.0189` n `25`; metal avg `-0.0942` n `20`; unknown avg `-0.0591` n `793`
- 4h: commodity avg `-0.0434` n `12`; crypto_alt avg `1.4107` n `230`; crypto_major avg `0.469` n `8`; equity avg `-0.7528` n `121`; fx avg `-0.0272` n `6`; index avg `-0.0864` n `25`; metal avg `-0.0828` n `20`; unknown avg `0.1676` n `793`
- 24h: commodity avg `0.2861` n `12`; crypto_alt avg `8.6374` n `230`; crypto_major avg `6.7114` n `8`; equity avg `0.7044` n `121`; fx avg `-0.0932` n `6`; index avg `0.0` n `25`; metal avg `0.5778` n `20`; unknown avg `3.2254` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2356`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
