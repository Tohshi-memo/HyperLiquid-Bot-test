# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T00:07:33.749634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0462` n `230`; crypto_major avg `-0.1259` n `8`; equity avg `-0.0402` n `113`; fx avg `0.011` n `6`; index avg `-0.0465` n `25`; metal avg `0.055` n `20`; unknown avg `-0.037` n `785`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.2042` n `8`; equity avg `-0.0898` n `113`; fx avg `0.0034` n `6`; index avg `-0.061` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.0164` n `785`
- 4h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.3558` n `230`; crypto_major avg `-0.5772` n `8`; equity avg `-0.27` n `113`; fx avg `0.0004` n `6`; index avg `-0.0809` n `25`; metal avg `0.0785` n `20`; unknown avg `1.6526` n `785`
- 24h: commodity avg `0.8833` n `12`; crypto_alt avg `-0.4157` n `230`; crypto_major avg `-0.6529` n `8`; equity avg `-1.9755` n `113`; fx avg `0.248` n `6`; index avg `-0.1509` n `25`; metal avg `0.3953` n `20`; unknown avg `103.6416` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
