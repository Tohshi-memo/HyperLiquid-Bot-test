# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T02:22:29.077663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `13`; crypto_alt avg `0.0645` n `235`; crypto_major avg `0.0664` n `8`; equity avg `-0.033` n `150`; fx avg `0.0054` n `6`; index avg `-0.0019` n `26`; metal avg `0.0122` n `20`; unknown avg `0.0421` n `1077`
- 1h: commodity avg `0.0638` n `13`; crypto_alt avg `-0.171` n `235`; crypto_major avg `-0.0495` n `8`; equity avg `-0.0031` n `150`; fx avg `0.0249` n `6`; index avg `0.0284` n `26`; metal avg `0.1147` n `20`; unknown avg `-0.0177` n `1075`
- 4h: commodity avg `0.1207` n `13`; crypto_alt avg `0.6979` n `235`; crypto_major avg `0.3405` n `8`; equity avg `-0.0013` n `150`; fx avg `-0.0276` n `6`; index avg `-0.0221` n `26`; metal avg `0.3907` n `20`; unknown avg `0.6457` n `1069`
- 24h: commodity avg `0.4249` n `13`; crypto_alt avg `-0.5308` n `235`; crypto_major avg `-1.0932` n `8`; equity avg `-0.6321` n `150`; fx avg `-0.179` n `6`; index avg `-0.1353` n `26`; metal avg `-0.133` n `20`; unknown avg `247.8694` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
