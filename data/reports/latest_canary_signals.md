# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T01:07:32.378051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.4381` n `234`; crypto_major avg `0.2048` n `8`; equity avg `0.0927` n `141`; fx avg `-0.0067` n `6`; index avg `0.0147` n `26`; metal avg `0.0618` n `20`; unknown avg `0.1789` n `944`
- 1h: commodity avg `-0.0485` n `12`; crypto_alt avg `0.1421` n `234`; crypto_major avg `0.0904` n `8`; equity avg `0.1336` n `141`; fx avg `-0.0242` n `6`; index avg `0.0056` n `26`; metal avg `0.0357` n `20`; unknown avg `0.4628` n `944`
- 4h: commodity avg `-0.359` n `12`; crypto_alt avg `0.6106` n `234`; crypto_major avg `0.2879` n `8`; equity avg `0.1502` n `141`; fx avg `-0.0316` n `6`; index avg `0.0124` n `26`; metal avg `0.011` n `20`; unknown avg `4.7435` n `898`
- 24h: commodity avg `0.6126` n `12`; crypto_alt avg `4.1319` n `234`; crypto_major avg `1.1394` n `8`; equity avg `-0.0619` n `141`; fx avg `-0.0134` n `6`; index avg `-0.088` n `26`; metal avg `-0.1188` n `20`; unknown avg `24.3194` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
