# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T16:59:08.583528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `0.1493` n `230`; crypto_major avg `0.2887` n `8`; equity avg `-0.0152` n `121`; fx avg `-0.0046` n `6`; index avg `-0.0018` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0321` n `794`
- 1h: commodity avg `0.0152` n `12`; crypto_alt avg `1.0439` n `230`; crypto_major avg `1.0877` n `8`; equity avg `0.03` n `121`; fx avg `0.0044` n `6`; index avg `-0.0035` n `25`; metal avg `0.0051` n `20`; unknown avg `0.2059` n `794`
- 4h: commodity avg `-0.0498` n `12`; crypto_alt avg `0.0058` n `230`; crypto_major avg `-0.1088` n `8`; equity avg `-0.0691` n `121`; fx avg `0.0006` n `6`; index avg `-0.0053` n `25`; metal avg `0.0115` n `20`; unknown avg `0.1896` n `794`
- 24h: commodity avg `-0.0719` n `12`; crypto_alt avg `0.5492` n `230`; crypto_major avg `2.8218` n `8`; equity avg `-0.511` n `121`; fx avg `0.0609` n `6`; index avg `-0.0633` n `25`; metal avg `-0.1843` n `20`; unknown avg `0.4495` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
