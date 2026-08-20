# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T19:37:31.478606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.0982` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `0.1638` n `121`; fx avg `-0.0005` n `6`; index avg `0.0149` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.0942` n `792`
- 1h: commodity avg `-0.0206` n `12`; crypto_alt avg `0.2149` n `230`; crypto_major avg `0.0612` n `8`; equity avg `0.5267` n `121`; fx avg `-0.01` n `6`; index avg `0.0604` n `25`; metal avg `0.0569` n `20`; unknown avg `-0.1398` n `792`
- 4h: commodity avg `0.0728` n `12`; crypto_alt avg `0.0263` n `230`; crypto_major avg `0.2836` n `8`; equity avg `0.1958` n `121`; fx avg `0.0202` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0005` n `20`; unknown avg `1.0753` n `792`
- 24h: commodity avg `0.4675` n `12`; crypto_alt avg `5.3314` n `230`; crypto_major avg `7.3959` n `8`; equity avg `-0.3578` n `121`; fx avg `0.209` n `6`; index avg `-0.0197` n `25`; metal avg `0.2041` n `20`; unknown avg `3.3426` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
