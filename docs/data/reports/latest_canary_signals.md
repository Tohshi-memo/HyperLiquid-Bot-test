# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T21:22:33.159131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0153` n `12`; crypto_alt avg `0.0623` n `232`; crypto_major avg `-0.0001` n `8`; equity avg `0.182` n `133`; fx avg `-0.0058` n `6`; index avg `0.0204` n `26`; metal avg `0.0071` n `20`; unknown avg `0.0082` n `788`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.0712` n `232`; crypto_major avg `-0.0394` n `8`; equity avg `0.25` n `133`; fx avg `-0.0078` n `6`; index avg `0.0143` n `26`; metal avg `0.0089` n `20`; unknown avg `0.1265` n `784`
- 4h: commodity avg `0.0211` n `12`; crypto_alt avg `0.443` n `232`; crypto_major avg `0.6621` n `8`; equity avg `0.6688` n `133`; fx avg `-0.0308` n `6`; index avg `0.0199` n `26`; metal avg `0.1418` n `20`; unknown avg `-0.0321` n `772`
- 24h: commodity avg `0.1836` n `12`; crypto_alt avg `-0.0584` n `232`; crypto_major avg `-0.0157` n `8`; equity avg `0.8849` n `133`; fx avg `-0.4061` n `6`; index avg `0.1049` n `26`; metal avg `0.4667` n `20`; unknown avg `0.3167` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
