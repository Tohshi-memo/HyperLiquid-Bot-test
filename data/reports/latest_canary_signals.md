# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T15:07:29.278699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.5645` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4686` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.028` n `13`; crypto_alt avg `-0.9621` n `239`; crypto_major avg `-1.1578` n `8`; equity avg `-0.2939` n `168`; fx avg `0.0085` n `6`; index avg `-0.0118` n `27`; metal avg `0.005` n `20`; unknown avg `-0.04` n `1257`
- 1h: commodity avg `0.0504` n `13`; crypto_alt avg `-1.3347` n `239`; crypto_major avg `-1.4895` n `8`; equity avg `-0.3721` n `168`; fx avg `-0.0227` n `6`; index avg `-0.0209` n `27`; metal avg `0.075` n `20`; unknown avg `1.0165` n `1261`
- 4h: commodity avg `0.0795` n `13`; crypto_alt avg `-1.0699` n `239`; crypto_major avg `-0.9072` n `8`; equity avg `0.0587` n `168`; fx avg `-0.0052` n `6`; index avg `0.0213` n `27`; metal avg `0.1283` n `20`; unknown avg `0.6466` n `1249`
- 24h: commodity avg `0.199` n `13`; crypto_alt avg `3.9254` n `239`; crypto_major avg `3.1102` n `8`; equity avg `5.0715` n `168`; fx avg `0.0756` n `6`; index avg `0.4622` n `27`; metal avg `1.2008` n `20`; unknown avg `3.0718` n `1055`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
