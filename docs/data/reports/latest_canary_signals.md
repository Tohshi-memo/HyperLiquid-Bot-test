# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T16:22:24.600146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8933` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0322` n `13`; crypto_alt avg `-0.0376` n `239`; crypto_major avg `-0.0094` n `8`; equity avg `-0.0801` n `168`; fx avg `-0.0146` n `6`; index avg `-0.0257` n `27`; metal avg `0.0013` n `20`; unknown avg `0.0763` n `1262`
- 1h: commodity avg `-0.1887` n `13`; crypto_alt avg `0.4932` n `239`; crypto_major avg `0.6621` n `8`; equity avg `0.7205` n `168`; fx avg `-0.018` n `6`; index avg `0.0755` n `27`; metal avg `-0.0424` n `20`; unknown avg `-0.1335` n `1252`
- 4h: commodity avg `-0.3606` n `13`; crypto_alt avg `-1.7009` n `239`; crypto_major avg `-1.9303` n `8`; equity avg `-0.6419` n `168`; fx avg `-0.0769` n `6`; index avg `-0.037` n `27`; metal avg `-0.4548` n `20`; unknown avg `0.9515` n `1251`
- 24h: commodity avg `-0.5345` n `13`; crypto_alt avg `0.352` n `239`; crypto_major avg `1.1518` n `8`; equity avg `2.7308` n `168`; fx avg `-0.145` n `6`; index avg `0.25` n `27`; metal avg `0.6355` n `20`; unknown avg `286.3562` n `1041`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
