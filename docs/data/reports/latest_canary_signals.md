# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T10:52:29.812831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `-0.0599` n `233`; crypto_major avg `-0.0003` n `8`; equity avg `0.0244` n `136`; fx avg `0.0102` n `6`; index avg `0.0046` n `27`; metal avg `-0.0075` n `20`; unknown avg `0.1243` n `894`
- 1h: commodity avg `-0.0692` n `12`; crypto_alt avg `-0.2875` n `233`; crypto_major avg `-0.2823` n `8`; equity avg `0.2229` n `136`; fx avg `0.0301` n `6`; index avg `0.0546` n `27`; metal avg `0.0806` n `20`; unknown avg `0.6031` n `892`
- 4h: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.3484` n `233`; crypto_major avg `0.2091` n `8`; equity avg `-0.4465` n `136`; fx avg `-0.0128` n `6`; index avg `-0.0648` n `27`; metal avg `-0.3404` n `20`; unknown avg `5.4221` n `862`
- 24h: commodity avg `0.5814` n `12`; crypto_alt avg `0.4804` n `233`; crypto_major avg `2.0056` n `8`; equity avg `-0.692` n `136`; fx avg `0.0446` n `6`; index avg `-0.2047` n `27`; metal avg `-0.4596` n `20`; unknown avg `0.9494` n `650`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
