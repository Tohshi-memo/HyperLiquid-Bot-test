# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T16:48:11.438896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `12`; crypto_alt avg `0.1089` n `230`; crypto_major avg `0.0481` n `8`; equity avg `-0.0117` n `121`; fx avg `-0.0019` n `6`; index avg `0.0001` n `25`; metal avg `0.0419` n `20`; unknown avg `-0.0139` n `793`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `0.2364` n `230`; crypto_major avg `0.0094` n `8`; equity avg `-0.2825` n `121`; fx avg `0.0085` n `6`; index avg `-0.0618` n `25`; metal avg `0.088` n `20`; unknown avg `1.2873` n `793`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `0.7451` n `230`; crypto_major avg `0.7384` n `8`; equity avg `-0.5752` n `121`; fx avg `0.0035` n `6`; index avg `-0.0711` n `25`; metal avg `0.0862` n `20`; unknown avg `1.3839` n `793`
- 24h: commodity avg `0.341` n `12`; crypto_alt avg `7.1205` n `230`; crypto_major avg `3.9693` n `8`; equity avg `1.1622` n `121`; fx avg `-0.0956` n `6`; index avg `0.0677` n `25`; metal avg `0.6618` n `20`; unknown avg `2.8951` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2378`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
