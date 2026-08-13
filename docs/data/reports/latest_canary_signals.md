# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T19:07:32.615570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `12`; crypto_alt avg `0.2108` n `230`; crypto_major avg `0.2282` n `8`; equity avg `0.1527` n `113`; fx avg `-0.0013` n `6`; index avg `0.0038` n `25`; metal avg `0.0054` n `20`; unknown avg `0.1404` n `787`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `0.1371` n `230`; crypto_major avg `0.3575` n `8`; equity avg `0.2967` n `113`; fx avg `-0.0023` n `6`; index avg `0.0339` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.2407` n `787`
- 4h: commodity avg `-0.2047` n `12`; crypto_alt avg `-0.6304` n `230`; crypto_major avg `-0.1673` n `8`; equity avg `0.1051` n `113`; fx avg `-0.0099` n `6`; index avg `0.0112` n `25`; metal avg `-0.0582` n `20`; unknown avg `-0.0986` n `787`
- 24h: commodity avg `-0.5556` n `12`; crypto_alt avg `-0.3612` n `230`; crypto_major avg `0.2698` n `8`; equity avg `1.5371` n `113`; fx avg `0.0049` n `6`; index avg `0.3238` n `25`; metal avg `-0.5133` n `20`; unknown avg `0.0315` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.232`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
