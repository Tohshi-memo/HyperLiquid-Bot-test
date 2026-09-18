# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T07:52:28.767754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0697` n `12`; crypto_alt avg `0.1369` n `234`; crypto_major avg `0.1182` n `8`; equity avg `-0.0599` n `140`; fx avg `0.0232` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.0809` n `927`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `0.4375` n `234`; crypto_major avg `0.4121` n `8`; equity avg `0.0614` n `140`; fx avg `0.0603` n `6`; index avg `0.0226` n `26`; metal avg `0.1209` n `20`; unknown avg `-0.0261` n `925`
- 4h: commodity avg `-0.1836` n `12`; crypto_alt avg `0.3392` n `234`; crypto_major avg `0.5659` n `8`; equity avg `0.5367` n `140`; fx avg `0.011` n `6`; index avg `0.0917` n `26`; metal avg `0.34` n `20`; unknown avg `-0.0414` n `863`
- 24h: commodity avg `-0.3526` n `12`; crypto_alt avg `5.2741` n `234`; crypto_major avg `3.9651` n `8`; equity avg `2.2019` n `140`; fx avg `0.17` n `6`; index avg `0.3266` n `26`; metal avg `0.593` n `20`; unknown avg `2.7846` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
