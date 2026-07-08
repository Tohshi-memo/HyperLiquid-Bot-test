# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T03:52:25.407116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.8085` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6793` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4913` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.2003` n `229`; crypto_major avg `-0.2042` n `8`; equity avg `-0.1671` n `91`; fx avg `0.0107` n `6`; index avg `-0.0749` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.2115` n `763`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `-0.0539` n `229`; crypto_major avg `-0.2045` n `8`; equity avg `0.3347` n `91`; fx avg `0.0154` n `6`; index avg `0.0154` n `25`; metal avg `0.1891` n `20`; unknown avg `0.1794` n `763`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.9876` n `229`; crypto_major avg `-1.3723` n `8`; equity avg `1.4362` n `91`; fx avg `-0.0778` n `6`; index avg `0.119` n `25`; metal avg `0.307` n `20`; unknown avg `0.0133` n `763`
- 24h: commodity avg `0.9331` n `12`; crypto_alt avg `-2.4384` n `229`; crypto_major avg `-1.8703` n `8`; equity avg `-0.7178` n `91`; fx avg `-0.1586` n `6`; index avg `-0.0844` n `25`; metal avg `0.0265` n `20`; unknown avg `-0.3721` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
