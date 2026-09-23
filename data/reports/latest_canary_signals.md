# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T05:22:29.471983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.0921` n `234`; crypto_major avg `-0.1692` n `8`; equity avg `-0.0157` n `140`; fx avg `0.0136` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0319` n `20`; unknown avg `-0.0844` n `945`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `0.1604` n `234`; crypto_major avg `-0.5179` n `8`; equity avg `-0.0643` n `140`; fx avg `0.0062` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0359` n `20`; unknown avg `0.1893` n `943`
- 4h: commodity avg `-0.1905` n `12`; crypto_alt avg `0.709` n `234`; crypto_major avg `0.3559` n `8`; equity avg `-0.1731` n `140`; fx avg `-0.0108` n `6`; index avg `-0.025` n `26`; metal avg `-0.0868` n `20`; unknown avg `-0.5031` n `937`
- 24h: commodity avg `-0.1857` n `12`; crypto_alt avg `4.6998` n `234`; crypto_major avg `2.753` n `8`; equity avg `1.2492` n `140`; fx avg `-0.1647` n `6`; index avg `0.1207` n `26`; metal avg `0.1524` n `20`; unknown avg `2.5422` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
