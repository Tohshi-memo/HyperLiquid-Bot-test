# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T08:22:32.887133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `-0.108` n `234`; crypto_major avg `-0.0641` n `8`; equity avg `0.0007` n `141`; fx avg `0.0` n `6`; index avg `0.0007` n `26`; metal avg `-0.0045` n `20`; unknown avg `0.0036` n `961`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.1927` n `234`; crypto_major avg `-0.11` n `8`; equity avg `0.0079` n `141`; fx avg `0.0106` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.0036` n `943`
- 4h: commodity avg `-0.0548` n `12`; crypto_alt avg `0.4005` n `234`; crypto_major avg `-0.2199` n `8`; equity avg `0.0346` n `141`; fx avg `0.0177` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0097` n `20`; unknown avg `3.6962` n `919`
- 24h: commodity avg `-0.0381` n `12`; crypto_alt avg `2.2428` n `234`; crypto_major avg `0.1858` n `8`; equity avg `-0.7797` n `141`; fx avg `-0.0824` n `6`; index avg `0.0312` n `26`; metal avg `0.1396` n `20`; unknown avg `1122.7404` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
