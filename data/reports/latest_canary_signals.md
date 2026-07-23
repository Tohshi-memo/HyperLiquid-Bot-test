# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T23:22:28.370338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.0175` n `230`; crypto_major avg `0.0618` n `8`; equity avg `0.0469` n `100`; fx avg `-0.0009` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0473` n `772`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `0.0431` n `230`; crypto_major avg `0.1566` n `8`; equity avg `0.1071` n `100`; fx avg `0.0069` n `6`; index avg `0.0342` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0037` n `772`
- 4h: commodity avg `0.0392` n `12`; crypto_alt avg `0.0264` n `230`; crypto_major avg `0.3143` n `8`; equity avg `0.3592` n `100`; fx avg `-0.0003` n `6`; index avg `0.0781` n `25`; metal avg `0.0134` n `20`; unknown avg `0.3215` n `772`
- 24h: commodity avg `0.6774` n `12`; crypto_alt avg `-1.3043` n `230`; crypto_major avg `-1.7777` n `8`; equity avg `-0.9888` n `99`; fx avg `-0.0656` n `6`; index avg `-0.1944` n `25`; metal avg `-0.6781` n `20`; unknown avg `-0.2585` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
