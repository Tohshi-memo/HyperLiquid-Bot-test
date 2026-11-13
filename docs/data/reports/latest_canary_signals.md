# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T03:07:36.277714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5821` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3259` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0177` n `13`; crypto_alt avg `0.2671` n `239`; crypto_major avg `0.2701` n `8`; equity avg `-0.0059` n `162`; fx avg `0.0013` n `6`; index avg `0.008` n `27`; metal avg `0.0338` n `20`; unknown avg `0.1029` n `1254`
- 1h: commodity avg `0.0405` n `13`; crypto_alt avg `-0.9425` n `239`; crypto_major avg `-0.9188` n `8`; equity avg `-0.8007` n `162`; fx avg `0.0012` n `6`; index avg `-0.062` n `27`; metal avg `0.0087` n `20`; unknown avg `0.6873` n `1256`
- 4h: commodity avg `-0.1499` n `13`; crypto_alt avg `-1.0502` n `239`; crypto_major avg `-1.3015` n `8`; equity avg `-0.3304` n `162`; fx avg `-0.0231` n `6`; index avg `0.0244` n `27`; metal avg `0.2806` n `20`; unknown avg `-0.0263` n `1247`
- 24h: commodity avg `0.7955` n `13`; crypto_alt avg `-1.629` n `239`; crypto_major avg `-2.9093` n `8`; equity avg `-1.2762` n `162`; fx avg `-0.0324` n `6`; index avg `0.019` n `27`; metal avg `-0.4183` n `20`; unknown avg `50.7876` n `1119`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
