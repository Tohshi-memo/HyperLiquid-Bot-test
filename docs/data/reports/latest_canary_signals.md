# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T05:22:36.744670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0668` n `230`; crypto_major avg `0.0346` n `8`; equity avg `0.0633` n `113`; fx avg `0.0017` n `6`; index avg `0.0029` n `25`; metal avg `0.0419` n `20`; unknown avg `0.4283` n `787`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `0.1455` n `230`; crypto_major avg `0.3518` n `8`; equity avg `0.2437` n `113`; fx avg `-0.0127` n `6`; index avg `0.0305` n `25`; metal avg `0.0772` n `20`; unknown avg `2.6115` n `787`
- 4h: commodity avg `0.1555` n `12`; crypto_alt avg `0.4247` n `230`; crypto_major avg `0.7073` n `8`; equity avg `0.4149` n `113`; fx avg `0.0136` n `6`; index avg `0.041` n `25`; metal avg `-0.1195` n `20`; unknown avg `1.5406` n `786`
- 24h: commodity avg `-0.1228` n `12`; crypto_alt avg `-0.9636` n `230`; crypto_major avg `0.1625` n `8`; equity avg `2.8062` n `113`; fx avg `-0.0367` n `6`; index avg `0.3581` n `25`; metal avg `-0.0522` n `20`; unknown avg `0.4118` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
