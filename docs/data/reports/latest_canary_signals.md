# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T18:22:24.073015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `0.1747` n `235`; crypto_major avg `-0.0013` n `8`; equity avg `-0.0113` n `150`; fx avg `0.0005` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0018` n `20`; unknown avg `2.3936` n `1117`
- 1h: commodity avg `-0.0266` n `13`; crypto_alt avg `0.1346` n `235`; crypto_major avg `-0.0139` n `8`; equity avg `-0.0103` n `150`; fx avg `0.0012` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0036` n `20`; unknown avg `3.8012` n `1075`
- 4h: commodity avg `-0.0086` n `13`; crypto_alt avg `0.7148` n `235`; crypto_major avg `0.0686` n `8`; equity avg `0.0499` n `150`; fx avg `-0.0025` n `6`; index avg `-0.003` n `26`; metal avg `-0.026` n `20`; unknown avg `1.0352` n `1053`
- 24h: commodity avg `-0.3642` n `13`; crypto_alt avg `2.5887` n `235`; crypto_major avg `0.8452` n `8`; equity avg `0.116` n `150`; fx avg `-0.0106` n `6`; index avg `0.0106` n `26`; metal avg `-0.0415` n `20`; unknown avg `1.2714` n `944`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
