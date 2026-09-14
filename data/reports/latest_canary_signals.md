# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T04:07:33.964753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0612` n `12`; crypto_alt avg `0.0527` n `233`; crypto_major avg `0.1092` n `8`; equity avg `0.0131` n `136`; fx avg `-0.019` n `6`; index avg `0.0055` n `27`; metal avg `-0.004` n `20`; unknown avg `0.4143` n `892`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.0515` n `233`; crypto_major avg `0.0484` n `8`; equity avg `-0.0999` n `136`; fx avg `-0.0406` n `6`; index avg `-0.0346` n `27`; metal avg `-0.0392` n `20`; unknown avg `7.7923` n `886`
- 4h: commodity avg `0.0656` n `12`; crypto_alt avg `1.2211` n `233`; crypto_major avg `1.3509` n `8`; equity avg `-0.0819` n `136`; fx avg `-0.0355` n `6`; index avg `0.062` n `27`; metal avg `-0.0768` n `20`; unknown avg `23.0121` n `762`
- 24h: commodity avg `0.7055` n `12`; crypto_alt avg `-0.5432` n `233`; crypto_major avg `0.0242` n `8`; equity avg `-1.3664` n `136`; fx avg `0.0301` n `6`; index avg `-0.3119` n `26`; metal avg `-0.1577` n `20`; unknown avg `1.7462` n `676`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
