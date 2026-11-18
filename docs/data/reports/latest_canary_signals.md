# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T08:07:44.063080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `13`; crypto_alt avg `0.0145` n `239`; crypto_major avg `-0.0905` n `8`; equity avg `-0.1234` n `163`; fx avg `-0.0057` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0796` n `20`; unknown avg `6.4866` n `1242`
- 1h: commodity avg `0.137` n `13`; crypto_alt avg `0.0395` n `239`; crypto_major avg `0.1952` n `8`; equity avg `0.2962` n `163`; fx avg `-0.033` n `6`; index avg `0.0396` n `27`; metal avg `-0.1435` n `20`; unknown avg `0.8057` n `1246`
- 4h: commodity avg `-0.1661` n `13`; crypto_alt avg `0.536` n `239`; crypto_major avg `0.6643` n `8`; equity avg `0.7515` n `163`; fx avg `-0.0578` n `6`; index avg `0.0848` n `27`; metal avg `-0.2289` n `20`; unknown avg `3.967` n `1214`
- 24h: commodity avg `-0.0822` n `13`; crypto_alt avg `0.5143` n `239`; crypto_major avg `0.9` n `8`; equity avg `0.8727` n `163`; fx avg `-0.1278` n `6`; index avg `0.0654` n `27`; metal avg `-0.9583` n `20`; unknown avg `6.6286` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
