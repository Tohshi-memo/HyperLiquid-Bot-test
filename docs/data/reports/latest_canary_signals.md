# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T11:52:29.783955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `0.02` n `230`; crypto_major avg `-0.0608` n `8`; equity avg `0.0287` n `114`; fx avg `0.0051` n `6`; index avg `0.0092` n `25`; metal avg `-0.051` n `20`; unknown avg `0.0201` n `792`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `0.1131` n `230`; crypto_major avg `-0.0903` n `8`; equity avg `-0.178` n `114`; fx avg `0.0223` n `6`; index avg `-0.004` n `25`; metal avg `-0.0228` n `20`; unknown avg `0.0826` n `792`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `0.021` n `230`; crypto_major avg `0.0032` n `8`; equity avg `-0.1113` n `114`; fx avg `-0.0099` n `6`; index avg `-0.0141` n `25`; metal avg `-0.1071` n `20`; unknown avg `0.0264` n `792`
- 24h: commodity avg `-0.1317` n `12`; crypto_alt avg `0.1192` n `230`; crypto_major avg `0.9056` n `8`; equity avg `1.1529` n `114`; fx avg `-0.0121` n `6`; index avg `0.1486` n `25`; metal avg `0.1564` n `20`; unknown avg `0.0502` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
