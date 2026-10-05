# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T07:22:32.593534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0491` n `13`; crypto_alt avg `-0.1308` n `235`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0495` n `144`; fx avg `-0.0016` n `6`; index avg `-0.0249` n `26`; metal avg `-0.0346` n `20`; unknown avg `0.9125` n `1079`
- 1h: commodity avg `0.1197` n `13`; crypto_alt avg `0.4484` n `235`; crypto_major avg `0.3456` n `8`; equity avg `-0.0593` n `144`; fx avg `0.0048` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0083` n `20`; unknown avg `0.5949` n `1077`
- 4h: commodity avg `0.0993` n `13`; crypto_alt avg `0.4773` n `235`; crypto_major avg `0.3338` n `8`; equity avg `-0.1151` n `144`; fx avg `0.0023` n `6`; index avg `-0.0358` n `26`; metal avg `0.1012` n `20`; unknown avg `-0.1591` n `980`
- 24h: commodity avg `-0.2279` n `13`; crypto_alt avg `0.8106` n `235`; crypto_major avg `1.3617` n `8`; equity avg `0.2784` n `144`; fx avg `-0.0799` n `6`; index avg `-0.0414` n `26`; metal avg `0.1734` n `20`; unknown avg `-0.1741` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
