# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T19:37:28.951457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0361` n `12`; crypto_alt avg `-0.0655` n `230`; crypto_major avg `-0.0734` n `8`; equity avg `-0.0894` n `98`; fx avg `-0.0009` n `6`; index avg `-0.0117` n `25`; metal avg `0.0135` n `20`; unknown avg `-0.0134` n `773`
- 1h: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.0123` n `230`; crypto_major avg `0.1624` n `8`; equity avg `0.0717` n `98`; fx avg `-0.0042` n `6`; index avg `-0.0091` n `25`; metal avg `0.0156` n `20`; unknown avg `0.0709` n `773`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `-0.506` n `230`; crypto_major avg `-0.2844` n `8`; equity avg `-0.688` n `98`; fx avg `0.007` n `6`; index avg `-0.0552` n `25`; metal avg `-0.1726` n `20`; unknown avg `0.0195` n `773`
- 24h: commodity avg `0.5291` n `12`; crypto_alt avg `-0.5416` n `230`; crypto_major avg `-0.7983` n `8`; equity avg `-0.5884` n `98`; fx avg `-0.054` n `6`; index avg `-0.1308` n `25`; metal avg `0.2696` n `20`; unknown avg `1.3972` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0903`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0752`, n `666`, weak_sample_signal
