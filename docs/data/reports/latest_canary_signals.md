# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T12:52:32.804477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0328` n `12`; crypto_alt avg `0.1025` n `230`; crypto_major avg `0.0054` n `8`; equity avg `-0.0115` n `99`; fx avg `-0.0115` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0145` n `20`; unknown avg `-0.0271` n `773`
- 1h: commodity avg `0.1855` n `12`; crypto_alt avg `-0.2888` n `230`; crypto_major avg `-0.6396` n `8`; equity avg `-0.8004` n `99`; fx avg `0.004` n `6`; index avg `-0.1509` n `25`; metal avg `-0.1784` n `20`; unknown avg `0.0939` n `772`
- 4h: commodity avg `0.3514` n `12`; crypto_alt avg `-0.3555` n `230`; crypto_major avg `-0.5443` n `8`; equity avg `-1.2067` n `99`; fx avg `-0.0251` n `6`; index avg `-0.2244` n `25`; metal avg `-0.2378` n `20`; unknown avg `-0.0168` n `772`
- 24h: commodity avg `0.9805` n `12`; crypto_alt avg `-0.3267` n `230`; crypto_major avg `-0.4553` n `8`; equity avg `-0.1797` n `99`; fx avg `-0.0807` n `6`; index avg `-0.0192` n `25`; metal avg `-0.6212` n `20`; unknown avg `9.7988` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0667`, n `666`, weak_sample_signal
