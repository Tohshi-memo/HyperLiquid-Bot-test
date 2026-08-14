# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T06:37:27.944897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.0338` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `0.0204` n `113`; fx avg `0.0372` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0265` n `20`; unknown avg `-0.0349` n `787`
- 1h: commodity avg `0.09` n `12`; crypto_alt avg `-0.049` n `230`; crypto_major avg `-0.2936` n `8`; equity avg `-0.0616` n `113`; fx avg `0.0597` n `6`; index avg `-0.0039` n `25`; metal avg `0.0915` n `20`; unknown avg `-0.0312` n `755`
- 4h: commodity avg `0.1867` n `12`; crypto_alt avg `-0.3754` n `230`; crypto_major avg `-0.537` n `8`; equity avg `-0.2085` n `113`; fx avg `0.0612` n `6`; index avg `-0.009` n `25`; metal avg `0.0464` n `20`; unknown avg `-0.1002` n `755`
- 24h: commodity avg `-0.2893` n `12`; crypto_alt avg `-0.4798` n `230`; crypto_major avg `-0.7416` n `8`; equity avg `0.9077` n `113`; fx avg `-0.0019` n `6`; index avg `0.2517` n `25`; metal avg `-0.2814` n `20`; unknown avg `0.9687` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2319`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
