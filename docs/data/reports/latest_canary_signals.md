# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T22:52:32.547371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.0807` n `232`; crypto_major avg `-0.1095` n `8`; equity avg `-0.0525` n `133`; fx avg `0.0147` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0259` n `20`; unknown avg `-0.1856` n `792`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.1968` n `232`; crypto_major avg `-0.283` n `8`; equity avg `-0.0789` n `133`; fx avg `0.0292` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0164` n `20`; unknown avg `16.5079` n `790`
- 4h: commodity avg `0.0787` n `12`; crypto_alt avg `-0.1761` n `232`; crypto_major avg `-0.1335` n `8`; equity avg `0.2331` n `133`; fx avg `-0.0164` n `6`; index avg `0.0213` n `26`; metal avg `0.0124` n `20`; unknown avg `-0.3127` n `772`
- 24h: commodity avg `0.1442` n `12`; crypto_alt avg `-0.2712` n `232`; crypto_major avg `-0.3965` n `8`; equity avg `1.0138` n `133`; fx avg `-0.3875` n `6`; index avg `0.1356` n `26`; metal avg `0.4477` n `20`; unknown avg `-0.538` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
