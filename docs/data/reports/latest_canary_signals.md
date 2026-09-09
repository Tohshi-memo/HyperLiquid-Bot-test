# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T07:07:26.038492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.2525` n `233`; crypto_major avg `0.2949` n `8`; equity avg `0.0509` n `134`; fx avg `-0.0244` n `6`; index avg `0.0054` n `26`; metal avg `0.0182` n `20`; unknown avg `0.1871` n `796`
- 1h: commodity avg `0.1009` n `12`; crypto_alt avg `0.7494` n `233`; crypto_major avg `0.6261` n `8`; equity avg `0.1239` n `134`; fx avg `0.004` n `6`; index avg `0.0076` n `26`; metal avg `0.0335` n `20`; unknown avg `0.5984` n `796`
- 4h: commodity avg `-0.0343` n `12`; crypto_alt avg `1.4799` n `233`; crypto_major avg `1.0798` n `8`; equity avg `0.0613` n `134`; fx avg `-0.0484` n `6`; index avg `-0.0058` n `26`; metal avg `0.1788` n `20`; unknown avg `1.0005` n `771`
- 24h: commodity avg `-0.1429` n `12`; crypto_alt avg `0.9397` n `232`; crypto_major avg `1.8263` n `8`; equity avg `1.0591` n `134`; fx avg `-0.1527` n `6`; index avg `0.0073` n `26`; metal avg `-0.0479` n `20`; unknown avg `0.1694` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
