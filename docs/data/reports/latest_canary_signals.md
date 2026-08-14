# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T04:22:29.332685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.1007` n `230`; crypto_major avg `0.0708` n `8`; equity avg `0.049` n `113`; fx avg `0.007` n `6`; index avg `0.0095` n `25`; metal avg `0.0295` n `20`; unknown avg `0.1211` n `787`
- 1h: commodity avg `0.0249` n `12`; crypto_alt avg `-0.0659` n `230`; crypto_major avg `-0.0633` n `8`; equity avg `-0.0456` n `113`; fx avg `0.0237` n `6`; index avg `-0.013` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.2267` n `787`
- 4h: commodity avg `0.0354` n `12`; crypto_alt avg `-0.308` n `230`; crypto_major avg `-0.1818` n `8`; equity avg `-0.2737` n `113`; fx avg `-0.0386` n `6`; index avg `-0.0641` n `25`; metal avg `-0.0952` n `20`; unknown avg `-0.2075` n `787`
- 24h: commodity avg `-0.406` n `12`; crypto_alt avg `-0.1663` n `230`; crypto_major avg `0.0109` n `8`; equity avg `0.8825` n `113`; fx avg `0.0053` n `6`; index avg `0.2258` n `25`; metal avg `-0.4661` n `20`; unknown avg `1.0237` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
