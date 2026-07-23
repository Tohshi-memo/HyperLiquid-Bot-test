# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T11:22:25.956933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `0.1451` n `230`; crypto_major avg `0.1137` n `8`; equity avg `-0.0971` n `99`; fx avg `-0.0011` n `6`; index avg `-0.0235` n `25`; metal avg `-0.0189` n `20`; unknown avg `0.0087` n `772`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `0.0761` n `230`; crypto_major avg `0.1392` n `8`; equity avg `-0.141` n `99`; fx avg `-0.009` n `6`; index avg `-0.0119` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.0347` n `772`
- 4h: commodity avg `0.1218` n `12`; crypto_alt avg `0.3496` n `230`; crypto_major avg `0.4551` n `8`; equity avg `0.2498` n `99`; fx avg `-0.0295` n `6`; index avg `0.0162` n `25`; metal avg `-0.19` n `20`; unknown avg `-0.0062` n `772`
- 24h: commodity avg `0.7332` n `12`; crypto_alt avg `-0.2836` n `230`; crypto_major avg `-0.1007` n `8`; equity avg `0.4508` n `99`; fx avg `-0.0943` n `6`; index avg `0.1389` n `25`; metal avg `-0.4392` n `20`; unknown avg `10.2434` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0775`, n `666`, weak_sample_signal
