# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T20:37:26.897769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0035` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `-0.0414` n `100`; fx avg `0.0062` n `6`; index avg `-0.0` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0301` n `772`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.305` n `230`; crypto_major avg `0.2759` n `8`; equity avg `0.4811` n `100`; fx avg `0.0008` n `6`; index avg `0.1131` n `25`; metal avg `0.034` n `20`; unknown avg `0.3275` n `772`
- 4h: commodity avg `-0.1254` n `12`; crypto_alt avg `-0.1492` n `230`; crypto_major avg `0.0535` n `8`; equity avg `-0.0662` n `100`; fx avg `0.0205` n `6`; index avg `0.0429` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.32` n `772`
- 24h: commodity avg `0.8314` n `12`; crypto_alt avg `-1.2773` n `230`; crypto_major avg `-1.7932` n `8`; equity avg `-0.9508` n `99`; fx avg `-0.0664` n `6`; index avg `-0.2417` n `25`; metal avg `-0.7935` n `20`; unknown avg `-0.3159` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
