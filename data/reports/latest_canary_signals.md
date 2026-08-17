# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T09:37:24.619087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `-0.0537` n `230`; crypto_major avg `0.0194` n `8`; equity avg `-0.0053` n `114`; fx avg `0.0128` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0616` n `792`
- 1h: commodity avg `0.0596` n `12`; crypto_alt avg `-0.0981` n `230`; crypto_major avg `-0.0635` n `8`; equity avg `-0.179` n `114`; fx avg `-0.0057` n `6`; index avg `-0.0236` n `25`; metal avg `-0.0591` n `20`; unknown avg `-0.0691` n `792`
- 4h: commodity avg `0.0951` n `12`; crypto_alt avg `-0.3019` n `230`; crypto_major avg `-0.0537` n `8`; equity avg `0.3264` n `114`; fx avg `-0.0128` n `6`; index avg `0.0329` n `25`; metal avg `-0.0671` n `20`; unknown avg `-0.0054` n `776`
- 24h: commodity avg `-0.0871` n `12`; crypto_alt avg `-0.3083` n `230`; crypto_major avg `0.4862` n `8`; equity avg `1.1419` n `114`; fx avg `-0.033` n `6`; index avg `0.1179` n `25`; metal avg `0.1507` n `20`; unknown avg `0.0509` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
