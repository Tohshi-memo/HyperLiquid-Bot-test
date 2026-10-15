# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T11:52:37.229159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `13`; crypto_alt avg `0.1212` n `236`; crypto_major avg `-0.1327` n `8`; equity avg `-0.0981` n `151`; fx avg `-0.0021` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0638` n `20`; unknown avg `2.1971` n `1136`
- 1h: commodity avg `0.0357` n `13`; crypto_alt avg `0.4358` n `236`; crypto_major avg `0.1775` n `8`; equity avg `0.2743` n `151`; fx avg `0.0168` n `6`; index avg `0.0396` n `26`; metal avg `-0.0204` n `20`; unknown avg `1.5762` n `1134`
- 4h: commodity avg `0.1427` n `13`; crypto_alt avg `0.3503` n `236`; crypto_major avg `-0.2268` n `8`; equity avg `-0.2395` n `151`; fx avg `0.0402` n `6`; index avg `-0.015` n `26`; metal avg `0.1053` n `20`; unknown avg `-0.1714` n `1038`
- 24h: commodity avg `-0.3241` n `13`; crypto_alt avg `-4.4349` n `236`; crypto_major avg `-3.5285` n `8`; equity avg `-5.7184` n `151`; fx avg `0.0677` n `6`; index avg `-0.9211` n `26`; metal avg `-0.4052` n `20`; unknown avg `2.1351` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0865`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0699`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
