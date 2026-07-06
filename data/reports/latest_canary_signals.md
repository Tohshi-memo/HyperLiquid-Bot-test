# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T11:42:47.843850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0186` n `229`; crypto_major avg `0.0168` n `8`; equity avg `-0.0258` n `88`; fx avg `0.0008` n `6`; index avg `0.0031` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.0341` n `765`
- 1h: commodity avg `0.0382` n `12`; crypto_alt avg `0.0013` n `229`; crypto_major avg `0.0718` n `8`; equity avg `-0.1309` n `88`; fx avg `0.0019` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0937` n `765`
- 4h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.0906` n `229`; crypto_major avg `-0.0959` n `8`; equity avg `-0.0606` n `88`; fx avg `-0.0091` n `6`; index avg `0.0089` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0837` n `765`
- 24h: commodity avg `-0.1635` n `12`; crypto_alt avg `0.4221` n `229`; crypto_major avg `0.8747` n `8`; equity avg `-0.7701` n `88`; fx avg `0.0806` n `6`; index avg `-0.0009` n `25`; metal avg `-0.1454` n `20`; unknown avg `1.103` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
