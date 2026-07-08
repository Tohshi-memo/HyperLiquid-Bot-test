# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T04:22:25.602129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9066` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.7535` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4404` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.0002` n `229`; crypto_major avg `0.0498` n `8`; equity avg `-0.0993` n `91`; fx avg `-0.002` n `6`; index avg `-0.0152` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0807` n `763`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `-0.4097` n `229`; crypto_major avg `-0.4289` n `8`; equity avg `-0.2498` n `91`; fx avg `0.0182` n `6`; index avg `-0.1188` n `25`; metal avg `-0.0377` n `20`; unknown avg `0.1374` n `763`
- 4h: commodity avg `-0.0835` n `12`; crypto_alt avg `-1.1876` n `229`; crypto_major avg `-1.464` n `8`; equity avg `0.4426` n `91`; fx avg `-0.0641` n `6`; index avg `-0.0236` n `25`; metal avg `0.2895` n `20`; unknown avg `0.075` n `763`
- 24h: commodity avg `0.9233` n `12`; crypto_alt avg `-2.5105` n `229`; crypto_major avg `-1.71` n `8`; equity avg `-0.7924` n `91`; fx avg `-0.1627` n `6`; index avg `-0.1278` n `25`; metal avg `-0.0367` n `20`; unknown avg `-0.4642` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
