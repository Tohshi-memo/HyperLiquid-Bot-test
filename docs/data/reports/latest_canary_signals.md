# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T09:22:18.863525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0557` n `228`; crypto_major avg `0.0815` n `8`; equity avg `0.0032` n `69`; fx avg `-0.0155` n `6`; index avg `0.0201` n `23`; metal avg `0.012` n `18`; unknown avg `-0.027` n `421`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.0135` n `228`; crypto_major avg `0.0887` n `8`; equity avg `0.0128` n `69`; fx avg `0.0197` n `6`; index avg `-0.0471` n `23`; metal avg `0.0021` n `18`; unknown avg `0.1199` n `421`
- 4h: commodity avg `-0.0734` n `12`; crypto_alt avg `-0.1091` n `228`; crypto_major avg `0.2533` n `8`; equity avg `0.1237` n `69`; fx avg `0.0115` n `6`; index avg `0.0574` n `23`; metal avg `0.0216` n `18`; unknown avg `-0.3772` n `401`
- 24h: commodity avg `-0.2316` n `12`; crypto_alt avg `0.9598` n `228`; crypto_major avg `1.5102` n `8`; equity avg `1.0041` n `69`; fx avg `0.1032` n `6`; index avg `0.0525` n `23`; metal avg `0.0154` n `18`; unknown avg `-0.0267` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
