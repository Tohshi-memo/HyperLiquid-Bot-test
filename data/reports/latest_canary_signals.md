# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T02:52:28.616233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `13`; crypto_alt avg `-0.025` n `235`; crypto_major avg `0.0005` n `8`; equity avg `0.0059` n `150`; fx avg `-0.0012` n `6`; index avg `0.0043` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0165` n `1116`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `0.193` n `235`; crypto_major avg `-0.0423` n `8`; equity avg `0.0` n `150`; fx avg `-0.0001` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.0613` n `1114`
- 4h: commodity avg `-0.0162` n `13`; crypto_alt avg `1.1923` n `235`; crypto_major avg `0.378` n `8`; equity avg `0.0839` n `150`; fx avg `0.0056` n `6`; index avg `0.0322` n `26`; metal avg `0.0155` n `20`; unknown avg `0.0462` n `1108`
- 24h: commodity avg `-0.1071` n `13`; crypto_alt avg `2.469` n `235`; crypto_major avg `0.2959` n `8`; equity avg `0.5079` n `150`; fx avg `-0.0254` n `6`; index avg `0.0806` n `26`; metal avg `0.1628` n `20`; unknown avg `12.9563` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
