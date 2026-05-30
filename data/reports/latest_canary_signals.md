# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T11:37:17.679402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `0.2933` n `228`; crypto_major avg `0.2645` n `8`; equity avg `-0.0506` n `69`; fx avg `-0.0027` n `6`; index avg `0.0145` n `23`; metal avg `-0.0124` n `18`; unknown avg `0.7768` n `421`
- 1h: commodity avg `0.0612` n `12`; crypto_alt avg `-0.0004` n `228`; crypto_major avg `0.1348` n `8`; equity avg `-0.0645` n `69`; fx avg `-0.0047` n `6`; index avg `0.0115` n `23`; metal avg `-0.024` n `18`; unknown avg `0.5221` n `421`
- 4h: commodity avg `0.0489` n `12`; crypto_alt avg `0.2282` n `228`; crypto_major avg `0.3809` n `8`; equity avg `0.0156` n `69`; fx avg `0.0177` n `6`; index avg `-0.0617` n `23`; metal avg `0.0158` n `18`; unknown avg `0.5844` n `421`
- 24h: commodity avg `-0.2784` n `12`; crypto_alt avg `1.803` n `228`; crypto_major avg `2.3551` n `8`; equity avg `1.3153` n `69`; fx avg `0.1056` n `6`; index avg `-0.0592` n `23`; metal avg `-0.0397` n `18`; unknown avg `0.598` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
