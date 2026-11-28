# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T13:37:24.937649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.84` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0089` n `13`; crypto_alt avg `-0.1986` n `239`; crypto_major avg `-0.1134` n `8`; equity avg `-0.0873` n `168`; fx avg `0.0105` n `6`; index avg `-0.0037` n `27`; metal avg `-0.0365` n `20`; unknown avg `0.9747` n `1265`
- 1h: commodity avg `0.0203` n `13`; crypto_alt avg `-0.4569` n `239`; crypto_major avg `-0.3063` n `8`; equity avg `-0.1836` n `168`; fx avg `-0.0202` n `6`; index avg `-0.0106` n `27`; metal avg `-0.047` n `20`; unknown avg `0.3363` n `1257`
- 4h: commodity avg `0.007` n `13`; crypto_alt avg `-0.6916` n `239`; crypto_major avg `-0.4817` n `8`; equity avg `-0.2128` n `168`; fx avg `-0.0144` n `6`; index avg `-0.0128` n `27`; metal avg `-0.0198` n `20`; unknown avg `301.8199` n `1247`
- 24h: commodity avg `-0.2567` n `13`; crypto_alt avg `-3.9632` n `239`; crypto_major avg `-3.4278` n `8`; equity avg `-0.2222` n `168`; fx avg `-0.0821` n `6`; index avg `0.0103` n `27`; metal avg `0.101` n `20`; unknown avg `191.329` n `1090`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
