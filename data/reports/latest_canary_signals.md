# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T07:43:09.896162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `-0.1162` n `8`; equity avg `-0.1064` n `98`; fx avg `0.0274` n `6`; index avg `-0.0446` n `25`; metal avg `-0.1538` n `20`; unknown avg `-0.0645` n `773`
- 1h: commodity avg `0.1836` n `12`; crypto_alt avg `-0.2216` n `230`; crypto_major avg `-0.4506` n `8`; equity avg `-0.3987` n `98`; fx avg `0.0465` n `6`; index avg `-0.0925` n `25`; metal avg `-0.3283` n `20`; unknown avg `0.0567` n `773`
- 4h: commodity avg `0.2256` n `12`; crypto_alt avg `0.0375` n `230`; crypto_major avg `-0.4711` n `8`; equity avg `-0.268` n `98`; fx avg `0.0451` n `6`; index avg `-0.0582` n `25`; metal avg `-0.4448` n `20`; unknown avg `-0.2491` n `741`
- 24h: commodity avg `0.6393` n `12`; crypto_alt avg `0.1197` n `230`; crypto_major avg `0.0567` n `8`; equity avg `0.2677` n `98`; fx avg `-0.048` n `6`; index avg `0.106` n `25`; metal avg `-0.3668` n `20`; unknown avg `1.4454` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0832`, n `666`, weak_sample_signal
