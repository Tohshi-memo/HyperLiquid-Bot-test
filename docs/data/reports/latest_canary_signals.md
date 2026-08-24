# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T03:37:28.606638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8007` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4688` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1237` n `231`; crypto_major avg `-0.1367` n `8`; equity avg `-0.1657` n `122`; fx avg `0.0052` n `6`; index avg `-0.0202` n `25`; metal avg `0.0652` n `20`; unknown avg `0.1282` n `793`
- 1h: commodity avg `0.0064` n `12`; crypto_alt avg `-0.8023` n `231`; crypto_major avg `-0.8954` n `8`; equity avg `-0.688` n `122`; fx avg `0.0069` n `6`; index avg `-0.1156` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.3072` n `793`
- 4h: commodity avg `-0.0901` n `12`; crypto_alt avg `-2.1812` n `231`; crypto_major avg `-1.6893` n `8`; equity avg `-1.8668` n `122`; fx avg `-0.0568` n `6`; index avg `-0.2205` n `25`; metal avg `0.1114` n `20`; unknown avg `1.1356` n `793`
- 24h: commodity avg `-0.2868` n `12`; crypto_alt avg `3.1944` n `231`; crypto_major avg `0.5586` n `8`; equity avg `-1.1505` n `122`; fx avg `-0.1929` n `6`; index avg `-0.1069` n `25`; metal avg `0.1927` n `20`; unknown avg `6.02` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
