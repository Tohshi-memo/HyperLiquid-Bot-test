# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T17:16:55.456417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.4874` n `230`; crypto_major avg `-0.519` n `8`; equity avg `-0.0735` n `121`; fx avg `-0.0021` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0236` n `20`; unknown avg `0.1131` n `793`
- 1h: commodity avg `0.0958` n `12`; crypto_alt avg `-0.0235` n `230`; crypto_major avg `0.0671` n `8`; equity avg `-0.0759` n `121`; fx avg `0.001` n `6`; index avg `0.0067` n `25`; metal avg `0.0602` n `20`; unknown avg `0.2131` n `793`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `0.8591` n `230`; crypto_major avg `0.6986` n `8`; equity avg `-0.3601` n `121`; fx avg `0.0083` n `6`; index avg `-0.0104` n `25`; metal avg `0.0362` n `20`; unknown avg `0.1988` n `793`
- 24h: commodity avg `0.345` n `12`; crypto_alt avg `6.5946` n `230`; crypto_major avg `3.5603` n `8`; equity avg `1.2874` n `121`; fx avg `-0.1026` n `6`; index avg `0.1181` n `25`; metal avg `0.6815` n `20`; unknown avg `1.1181` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
