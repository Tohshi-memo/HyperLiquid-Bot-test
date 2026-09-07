# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T05:07:29.765495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.3977` n `232`; crypto_major avg `0.1683` n `8`; equity avg `-0.0009` n `134`; fx avg `-0.0104` n `6`; index avg `-0.0035` n `26`; metal avg `0.0466` n `20`; unknown avg `1.3499` n `792`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `0.4862` n `232`; crypto_major avg `0.2197` n `8`; equity avg `0.0134` n `134`; fx avg `-0.0064` n `6`; index avg `0.0064` n `26`; metal avg `0.0035` n `20`; unknown avg `0.5819` n `786`
- 4h: commodity avg `0.1416` n `12`; crypto_alt avg `-0.2088` n `232`; crypto_major avg `-0.5097` n `8`; equity avg `0.2175` n `134`; fx avg `0.1268` n `6`; index avg `0.0151` n `26`; metal avg `-0.0351` n `20`; unknown avg `2.208` n `758`
- 24h: commodity avg `0.105` n `12`; crypto_alt avg `0.2349` n `232`; crypto_major avg `-0.6498` n `8`; equity avg `0.4813` n `134`; fx avg `0.0202` n `6`; index avg `0.0065` n `26`; metal avg `-0.1808` n `20`; unknown avg `73.4407` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
