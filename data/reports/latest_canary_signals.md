# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T04:22:29.608014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.1869` n `235`; crypto_major avg `0.0732` n `8`; equity avg `0.0053` n `150`; fx avg `0.0026` n `6`; index avg `0.0004` n `26`; metal avg `0.0117` n `20`; unknown avg `-0.0844` n `1078`
- 1h: commodity avg `-0.0674` n `13`; crypto_alt avg `0.2427` n `235`; crypto_major avg `0.2167` n `8`; equity avg `0.2698` n `150`; fx avg `0.0041` n `6`; index avg `0.0331` n `26`; metal avg `0.0414` n `20`; unknown avg `4.1381` n `1070`
- 4h: commodity avg `-0.2429` n `13`; crypto_alt avg `1.7378` n `235`; crypto_major avg `1.0283` n `8`; equity avg `0.5891` n `150`; fx avg `0.0049` n `6`; index avg `0.0987` n `26`; metal avg `0.3478` n `20`; unknown avg `2.5995` n `1070`
- 24h: commodity avg `0.0854` n `13`; crypto_alt avg `-0.7778` n `235`; crypto_major avg `-1.6576` n `8`; equity avg `-1.5294` n `150`; fx avg `0.1197` n `6`; index avg `-0.136` n `26`; metal avg `0.1642` n `20`; unknown avg `6.1762` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
