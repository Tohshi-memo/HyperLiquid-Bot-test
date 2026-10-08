# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T03:52:30.756835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `13`; crypto_alt avg `-0.1425` n `235`; crypto_major avg `-0.1384` n `8`; equity avg `-0.1564` n `150`; fx avg `-0.005` n `6`; index avg `-0.0277` n `26`; metal avg `-0.0015` n `20`; unknown avg `1.3996` n `1077`
- 1h: commodity avg `0.0379` n `13`; crypto_alt avg `-0.5703` n `235`; crypto_major avg `-0.5335` n `8`; equity avg `-0.5731` n `150`; fx avg `0.0025` n `6`; index avg `-0.1021` n `26`; metal avg `-0.0651` n `20`; unknown avg `1.3493` n `1075`
- 4h: commodity avg `0.2386` n `13`; crypto_alt avg `-0.3031` n `235`; crypto_major avg `-0.4405` n `8`; equity avg `-0.7052` n `150`; fx avg `-0.0197` n `6`; index avg `-0.1409` n `26`; metal avg `0.3198` n `20`; unknown avg `-0.1076` n `1069`
- 24h: commodity avg `0.4218` n `13`; crypto_alt avg `-0.9567` n `235`; crypto_major avg `-1.8267` n `8`; equity avg `-1.5302` n `150`; fx avg `-0.1368` n `6`; index avg `-0.2761` n `26`; metal avg `-0.208` n `20`; unknown avg `247.081` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
