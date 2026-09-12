# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T23:07:30.984309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0305` n `233`; crypto_major avg `0.0384` n `8`; equity avg `-0.0022` n `136`; fx avg `0.0025` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.3585` n `836`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.1228` n `233`; crypto_major avg `0.0299` n `8`; equity avg `-0.0232` n `136`; fx avg `-0.0005` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.1165` n `828`
- 4h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.3215` n `233`; crypto_major avg `-0.0924` n `8`; equity avg `-0.2901` n `136`; fx avg `-0.0092` n `6`; index avg `-0.0355` n `26`; metal avg `-0.0325` n `20`; unknown avg `0.4539` n `796`
- 24h: commodity avg `-0.0941` n `12`; crypto_alt avg `1.5111` n `233`; crypto_major avg `0.4138` n `8`; equity avg `-0.263` n `136`; fx avg `-0.0069` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.4755` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
