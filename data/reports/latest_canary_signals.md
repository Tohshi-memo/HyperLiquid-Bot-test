# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T09:07:27.620251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `13`; crypto_alt avg `-0.0544` n `235`; crypto_major avg `-0.0021` n `8`; equity avg `0.0071` n `150`; fx avg `0.0` n `6`; index avg `0.0011` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.0213` n `1115`
- 1h: commodity avg `0.0126` n `13`; crypto_alt avg `0.2085` n `235`; crypto_major avg `0.1046` n `8`; equity avg `0.0404` n `150`; fx avg `-0.0042` n `6`; index avg `0.0008` n `26`; metal avg `-0.0` n `20`; unknown avg `0.0075` n `1115`
- 4h: commodity avg `0.0157` n `13`; crypto_alt avg `0.3492` n `235`; crypto_major avg `-0.1216` n `8`; equity avg `0.0229` n `150`; fx avg `-0.004` n `6`; index avg `0.0069` n `26`; metal avg `0.0157` n `20`; unknown avg `0.1361` n `1083`
- 24h: commodity avg `0.1958` n `13`; crypto_alt avg `1.1307` n `235`; crypto_major avg `-0.197` n `8`; equity avg `0.0916` n `150`; fx avg `0.0012` n `6`; index avg `0.0057` n `26`; metal avg `0.0058` n `20`; unknown avg `0.625` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
