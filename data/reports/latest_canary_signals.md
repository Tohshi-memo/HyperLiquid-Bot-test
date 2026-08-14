# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T04:31:38.225006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.0653` n `230`; crypto_major avg `-0.0394` n `8`; equity avg `0.0386` n `113`; fx avg `0.0082` n `6`; index avg `0.0092` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0418` n `787`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.0083` n `230`; crypto_major avg `0.0436` n `8`; equity avg `-0.0139` n `113`; fx avg `0.0315` n `6`; index avg `0.0008` n `25`; metal avg `-0.0496` n `20`; unknown avg `-0.1619` n `787`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.2875` n `230`; crypto_major avg `-0.148` n `8`; equity avg `-0.3544` n `113`; fx avg `-0.0213` n `6`; index avg `-0.073` n `25`; metal avg `-0.0839` n `20`; unknown avg `-0.3893` n `787`
- 24h: commodity avg `-0.3878` n `12`; crypto_alt avg `-0.2662` n `230`; crypto_major avg `-0.1705` n `8`; equity avg `0.8609` n `113`; fx avg `0.0163` n `6`; index avg `0.2247` n `25`; metal avg `-0.5144` n `20`; unknown avg `0.9244` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2428`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
