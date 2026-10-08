# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T08:22:32.759692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1085` n `13`; crypto_alt avg `0.0544` n `235`; crypto_major avg `-0.1036` n `8`; equity avg `0.0814` n `150`; fx avg `-0.0126` n `6`; index avg `0.006` n `26`; metal avg `0.012` n `20`; unknown avg `0.0115` n `1077`
- 1h: commodity avg `0.1026` n `13`; crypto_alt avg `-0.294` n `235`; crypto_major avg `-0.329` n `8`; equity avg `-0.0178` n `150`; fx avg `0.0127` n `6`; index avg `0.0039` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.1608` n `1059`
- 4h: commodity avg `0.4531` n `13`; crypto_alt avg `0.7955` n `235`; crypto_major avg `0.4035` n `8`; equity avg `-0.494` n `150`; fx avg `0.0218` n `6`; index avg `-0.0969` n `26`; metal avg `-0.1496` n `20`; unknown avg `0.221` n `1031`
- 24h: commodity avg `0.8154` n `13`; crypto_alt avg `-0.8553` n `235`; crypto_major avg `-2.3092` n `8`; equity avg `-1.7889` n `150`; fx avg `0.0034` n `6`; index avg `-0.3166` n `26`; metal avg `-0.2071` n `20`; unknown avg `416.7013` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
