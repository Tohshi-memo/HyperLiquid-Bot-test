# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T07:37:24.656206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `12`; crypto_alt avg `0.0938` n `230`; crypto_major avg `-0.02` n `8`; equity avg `-0.0367` n `98`; fx avg `0.0147` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0559` n `20`; unknown avg `-0.0981` n `773`
- 1h: commodity avg `0.1695` n `12`; crypto_alt avg `-0.1498` n `230`; crypto_major avg `-0.3548` n `8`; equity avg `-0.3294` n `98`; fx avg `0.0338` n `6`; index avg `-0.0649` n `25`; metal avg `-0.231` n `20`; unknown avg `0.0191` n `773`
- 4h: commodity avg `0.2116` n `12`; crypto_alt avg `0.1094` n `230`; crypto_major avg `-0.3753` n `8`; equity avg `-0.1987` n `98`; fx avg `0.0324` n `6`; index avg `-0.0305` n `25`; metal avg `-0.3479` n `20`; unknown avg `-0.2885` n `741`
- 24h: commodity avg `0.6252` n `12`; crypto_alt avg `0.1917` n `230`; crypto_major avg `0.1534` n `8`; equity avg `0.3377` n `98`; fx avg `-0.0606` n `6`; index avg `0.1341` n `25`; metal avg `-0.2696` n `20`; unknown avg `1.3415` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
