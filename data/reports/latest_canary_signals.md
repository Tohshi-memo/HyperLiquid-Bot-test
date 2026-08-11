# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T15:22:33.916315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `0.0692` n `230`; crypto_major avg `0.0737` n `8`; equity avg `0.1218` n `113`; fx avg `0.009` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0354` n `20`; unknown avg `0.0151` n `785`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `-0.5974` n `230`; crypto_major avg `-0.4015` n `8`; equity avg `-0.0481` n `113`; fx avg `-0.0019` n `6`; index avg `-0.0095` n `25`; metal avg `0.0374` n `20`; unknown avg `-0.0359` n `785`
- 4h: commodity avg `0.0874` n `12`; crypto_alt avg `-0.8677` n `230`; crypto_major avg `-0.5838` n `8`; equity avg `0.3716` n `113`; fx avg `0.025` n `6`; index avg `-0.0066` n `25`; metal avg `-0.1607` n `20`; unknown avg `-0.0068` n `785`
- 24h: commodity avg `0.1691` n `12`; crypto_alt avg `-1.3171` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `0.4612` n `113`; fx avg `-0.0521` n `6`; index avg `0.1341` n `25`; metal avg `0.1671` n `20`; unknown avg `-0.2398` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1985`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
