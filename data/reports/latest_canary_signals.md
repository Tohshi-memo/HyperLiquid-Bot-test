# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T10:52:30.522640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `12`; crypto_alt avg `-0.0433` n `230`; crypto_major avg `-0.0842` n `8`; equity avg `-0.0031` n `98`; fx avg `0.0013` n `6`; index avg `0.0017` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.0098` n `773`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `-0.0465` n `230`; crypto_major avg `0.0775` n `8`; equity avg `0.1099` n `98`; fx avg `-0.0137` n `6`; index avg `0.0392` n `25`; metal avg `0.0342` n `20`; unknown avg `0.0339` n `773`
- 4h: commodity avg `0.1628` n `12`; crypto_alt avg `-0.0105` n `230`; crypto_major avg `0.0012` n `8`; equity avg `0.246` n `98`; fx avg `-0.0144` n `6`; index avg `0.0268` n `25`; metal avg `-0.2931` n `20`; unknown avg `0.0113` n `773`
- 24h: commodity avg `0.7291` n `12`; crypto_alt avg `-0.3751` n `230`; crypto_major avg `-0.2403` n `8`; equity avg `0.6619` n `98`; fx avg `-0.0847` n `6`; index avg `0.1594` n `25`; metal avg `-0.34` n `20`; unknown avg `11.4313` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0791`, n `666`, weak_sample_signal
