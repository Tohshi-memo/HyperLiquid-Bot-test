# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T04:52:25.561971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `-0.0016` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `-0.0304` n `113`; fx avg `0.0036` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.295` n `787`
- 1h: commodity avg `0.0227` n `12`; crypto_alt avg `0.1101` n `230`; crypto_major avg `0.0785` n `8`; equity avg `-0.0392` n `113`; fx avg `0.0286` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.1801` n `787`
- 4h: commodity avg `0.0668` n `12`; crypto_alt avg `-0.3088` n `230`; crypto_major avg `-0.3272` n `8`; equity avg `-0.2499` n `113`; fx avg `0.0008` n `6`; index avg `-0.0391` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.282` n `787`
- 24h: commodity avg `-0.3796` n `12`; crypto_alt avg `-0.2345` n `230`; crypto_major avg `-0.2426` n `8`; equity avg `0.7373` n `113`; fx avg `0.0356` n `6`; index avg `0.1909` n `25`; metal avg `-0.5351` n `20`; unknown avg `0.9036` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2439`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
