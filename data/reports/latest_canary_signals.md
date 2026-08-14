# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T05:52:30.260669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.0346` n `230`; crypto_major avg `-0.0289` n `8`; equity avg `0.0302` n `113`; fx avg `0.0006` n `6`; index avg `0.0111` n `25`; metal avg `0.0755` n `20`; unknown avg `0.4049` n `787`
- 1h: commodity avg `0.0799` n `12`; crypto_alt avg `-0.0483` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `-0.0021` n `113`; fx avg `-0.0339` n `6`; index avg `0.0268` n `25`; metal avg `0.0624` n `20`; unknown avg `0.178` n `787`
- 4h: commodity avg `0.17` n `12`; crypto_alt avg `-0.4054` n `230`; crypto_major avg `-0.2997` n `8`; equity avg `-0.0643` n `113`; fx avg `-0.0004` n `6`; index avg `0.0267` n `25`; metal avg `0.1284` n `20`; unknown avg `-0.3709` n `787`
- 24h: commodity avg `-0.3322` n `12`; crypto_alt avg `-0.482` n `230`; crypto_major avg `-0.62` n `8`; equity avg `0.7285` n `113`; fx avg `0.0016` n `6`; index avg `0.2377` n `25`; metal avg `-0.4215` n `20`; unknown avg `0.8731` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
