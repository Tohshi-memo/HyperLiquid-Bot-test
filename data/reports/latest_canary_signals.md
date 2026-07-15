# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T07:07:29.409990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0894` n `12`; crypto_alt avg `-0.1973` n `230`; crypto_major avg `-0.265` n `8`; equity avg `0.0469` n `93`; fx avg `0.0063` n `6`; index avg `-0.0043` n `25`; metal avg `0.0543` n `20`; unknown avg `-0.0143` n `767`
- 1h: commodity avg `0.0692` n `12`; crypto_alt avg `-0.2556` n `230`; crypto_major avg `-0.338` n `8`; equity avg `-0.1024` n `93`; fx avg `0.0133` n `6`; index avg `-0.048` n `25`; metal avg `0.039` n `20`; unknown avg `-0.1691` n `767`
- 4h: commodity avg `-0.0036` n `12`; crypto_alt avg `0.1816` n `230`; crypto_major avg `0.2652` n `8`; equity avg `0.1358` n `93`; fx avg `-0.0053` n `6`; index avg `-0.0013` n `25`; metal avg `-0.018` n `20`; unknown avg `0.1052` n `749`
- 24h: commodity avg `0.0888` n `12`; crypto_alt avg `1.5167` n `230`; crypto_major avg `3.2531` n `8`; equity avg `1.7606` n `92`; fx avg `0.0641` n `6`; index avg `0.504` n `25`; metal avg `0.2607` n `20`; unknown avg `0.2499` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
