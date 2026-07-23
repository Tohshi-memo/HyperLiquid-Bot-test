# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T18:22:26.554756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1505` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `0.0272` n `8`; equity avg `0.05` n `100`; fx avg `-0.0055` n `6`; index avg `0.0068` n `25`; metal avg `-0.0175` n `20`; unknown avg `-0.0208` n `772`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `-0.494` n `230`; crypto_major avg `-0.3393` n `8`; equity avg `-0.4285` n `100`; fx avg `0.0028` n `6`; index avg `-0.0458` n `25`; metal avg `-0.1077` n `20`; unknown avg `-0.3976` n `772`
- 4h: commodity avg `0.1664` n `12`; crypto_alt avg `-1.0609` n `230`; crypto_major avg `-1.0049` n `8`; equity avg `-0.8877` n `100`; fx avg `-0.0049` n `6`; index avg `-0.085` n `25`; metal avg `-0.1599` n `20`; unknown avg `-0.4775` n `772`
- 24h: commodity avg `0.9802` n `12`; crypto_alt avg `-1.7616` n `230`; crypto_major avg `-2.2334` n `8`; equity avg `-1.2173` n `99`; fx avg `-0.0879` n `6`; index avg `-0.3425` n `25`; metal avg `-0.8435` n `20`; unknown avg `-0.5267` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
