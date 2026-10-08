# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T00:22:31.524577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0322` n `13`; crypto_alt avg `0.2804` n `235`; crypto_major avg `0.0853` n `8`; equity avg `-0.0127` n `150`; fx avg `-0.0333` n `6`; index avg `-0.0051` n `26`; metal avg `-0.011` n `20`; unknown avg `0.0134` n `1077`
- 1h: commodity avg `0.0164` n `13`; crypto_alt avg `0.3779` n `235`; crypto_major avg `0.1514` n `8`; equity avg `0.005` n `150`; fx avg `-0.0705` n `6`; index avg `-0.0236` n `26`; metal avg `-0.0434` n `20`; unknown avg `-0.0339` n `1069`
- 4h: commodity avg `0.1248` n `13`; crypto_alt avg `0.93` n `235`; crypto_major avg `0.0621` n `8`; equity avg `0.186` n `150`; fx avg `-0.0608` n `6`; index avg `0.0164` n `26`; metal avg `-0.0155` n `20`; unknown avg `-0.0836` n `1019`
- 24h: commodity avg `0.334` n `13`; crypto_alt avg `-3.0701` n `235`; crypto_major avg `-3.0537` n `8`; equity avg `-1.4131` n `150`; fx avg `-0.2516` n `6`; index avg `-0.2405` n `26`; metal avg `-0.7157` n `20`; unknown avg `247.6795` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
