# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T13:37:26.327064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.045` n `13`; crypto_alt avg `-0.3625` n `235`; crypto_major avg `-0.4869` n `8`; equity avg `-0.4287` n `150`; fx avg `0.0025` n `6`; index avg `-0.0346` n `26`; metal avg `0.0811` n `20`; unknown avg `6.4944` n `1076`
- 1h: commodity avg `0.1513` n `13`; crypto_alt avg `-0.4596` n `235`; crypto_major avg `-0.7039` n `8`; equity avg `-0.3808` n `150`; fx avg `0.0056` n `6`; index avg `-0.0417` n `26`; metal avg `0.0765` n `20`; unknown avg `12.8615` n `1074`
- 4h: commodity avg `0.2175` n `13`; crypto_alt avg `-0.7536` n `235`; crypto_major avg `-0.686` n `8`; equity avg `-0.4148` n `150`; fx avg `-0.0521` n `6`; index avg `-0.0765` n `26`; metal avg `0.09` n `20`; unknown avg `5.9618` n `1068`
- 24h: commodity avg `-0.2661` n `13`; crypto_alt avg `-1.235` n `235`; crypto_major avg `-1.2368` n `8`; equity avg `-0.467` n `150`; fx avg `0.0188` n `6`; index avg `-0.0189` n `26`; metal avg `0.6355` n `20`; unknown avg `7.5523` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
