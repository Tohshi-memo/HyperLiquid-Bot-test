# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T07:52:25.117620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.2715` n `235`; crypto_major avg `-0.0091` n `8`; equity avg `-0.0196` n `150`; fx avg `0.0018` n `6`; index avg `-0.0014` n `26`; metal avg `0.0026` n `20`; unknown avg `2.9563` n `1117`
- 1h: commodity avg `-0.0161` n `13`; crypto_alt avg `-0.4452` n `235`; crypto_major avg `0.0053` n `8`; equity avg `-0.0452` n `150`; fx avg `0.0018` n `6`; index avg `-0.0158` n `26`; metal avg `0.0086` n `20`; unknown avg `2.767` n `1115`
- 4h: commodity avg `0.044` n `13`; crypto_alt avg `-0.0665` n `235`; crypto_major avg `0.2172` n `8`; equity avg `-0.0723` n `150`; fx avg `0.0078` n `6`; index avg `-0.0243` n `26`; metal avg `-0.0075` n `20`; unknown avg `1.6994` n `1092`
- 24h: commodity avg `0.0713` n `13`; crypto_alt avg `1.0853` n `235`; crypto_major avg `-0.0655` n `8`; equity avg `-0.2357` n `150`; fx avg `-0.0634` n `6`; index avg `-0.048` n `26`; metal avg `-0.0034` n `20`; unknown avg `666.7278` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
