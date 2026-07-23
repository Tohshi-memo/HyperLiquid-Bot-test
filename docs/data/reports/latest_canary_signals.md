# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T15:52:29.011061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0952` n `12`; crypto_alt avg `0.1606` n `230`; crypto_major avg `0.1774` n `8`; equity avg `0.1254` n `100`; fx avg `-0.0037` n `6`; index avg `0.0221` n `25`; metal avg `0.031` n `20`; unknown avg `0.0598` n `772`
- 1h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.136` n `230`; crypto_major avg `-0.0848` n `8`; equity avg `-0.393` n `100`; fx avg `-0.0026` n `6`; index avg `-0.0646` n `25`; metal avg `-0.0883` n `20`; unknown avg `0.0008` n `772`
- 4h: commodity avg `0.2077` n `12`; crypto_alt avg `-0.6396` n `230`; crypto_major avg `-1.1918` n `8`; equity avg `-1.3236` n `99`; fx avg `-0.0212` n `6`; index avg `-0.3145` n `25`; metal avg `-0.3379` n `20`; unknown avg `0.0778` n `772`
- 24h: commodity avg `1.0767` n `12`; crypto_alt avg `-1.2362` n `230`; crypto_major avg `-1.6245` n `8`; equity avg `-2.0776` n `99`; fx avg `-0.0854` n `6`; index avg `-0.4567` n `25`; metal avg `-0.9627` n `20`; unknown avg `-0.2538` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
