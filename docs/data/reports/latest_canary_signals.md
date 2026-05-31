# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T02:22:21.510285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `0.1016` n `228`; crypto_major avg `0.1617` n `8`; equity avg `0.0142` n `69`; fx avg `0.0162` n `6`; index avg `-0.0289` n `23`; metal avg `-0.047` n `18`; unknown avg `0.4276` n `421`
- 1h: commodity avg `-0.0632` n `12`; crypto_alt avg `0.3426` n `228`; crypto_major avg `0.188` n `8`; equity avg `0.0177` n `69`; fx avg `0.0192` n `6`; index avg `-0.0228` n `23`; metal avg `-0.0607` n `18`; unknown avg `1.074` n `421`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `0.7355` n `228`; crypto_major avg `0.9475` n `8`; equity avg `0.2896` n `69`; fx avg `0.0099` n `6`; index avg `0.0016` n `23`; metal avg `-0.0705` n `18`; unknown avg `-0.0597` n `421`
- 24h: commodity avg `-0.0458` n `12`; crypto_alt avg `0.438` n `228`; crypto_major avg `2.2363` n `8`; equity avg `0.9842` n `69`; fx avg `0.0494` n `6`; index avg `0.1097` n `23`; metal avg `-0.0506` n `18`; unknown avg `1.3334` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
