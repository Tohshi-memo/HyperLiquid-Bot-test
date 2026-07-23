# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T09:37:27.005349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `0.0185` n `230`; crypto_major avg `-0.031` n `8`; equity avg `-0.0692` n `98`; fx avg `0.0027` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0286` n `20`; unknown avg `0.0102` n `773`
- 1h: commodity avg `0.0522` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `0.0901` n `8`; equity avg `0.1712` n `98`; fx avg `-0.0205` n `6`; index avg `0.0235` n `25`; metal avg `-0.0217` n `20`; unknown avg `-0.0011` n `773`
- 4h: commodity avg `0.3167` n `12`; crypto_alt avg `0.1027` n `230`; crypto_major avg `-0.0043` n `8`; equity avg `-0.0191` n `98`; fx avg `0.0261` n `6`; index avg `-0.0677` n `25`; metal avg `-0.3966` n `20`; unknown avg `-0.0373` n `741`
- 24h: commodity avg `0.6673` n `12`; crypto_alt avg `0.0728` n `230`; crypto_major avg `0.1879` n `8`; equity avg `0.7633` n `98`; fx avg `-0.0834` n `6`; index avg `0.1702` n `25`; metal avg `-0.3628` n `20`; unknown avg `11.528` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0845`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
