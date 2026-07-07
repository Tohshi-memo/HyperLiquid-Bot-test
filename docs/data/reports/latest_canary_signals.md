# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T04:52:25.130807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5805` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5148` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `-0.115` n `229`; crypto_major avg `-0.1049` n `8`; equity avg `-0.1036` n `91`; fx avg `-0.0098` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.0819` n `763`
- 1h: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.1605` n `229`; crypto_major avg `-0.2758` n `8`; equity avg `-0.2496` n `91`; fx avg `-0.0026` n `6`; index avg `-0.0322` n `25`; metal avg `-0.0011` n `20`; unknown avg `12.7505` n `763`
- 4h: commodity avg `-0.0561` n `12`; crypto_alt avg `-1.5557` n `229`; crypto_major avg `-1.8351` n `8`; equity avg `-1.3109` n `91`; fx avg `-0.1002` n `6`; index avg `-0.3203` n `25`; metal avg `-0.2546` n `20`; unknown avg `17.0602` n `761`
- 24h: commodity avg `0.2475` n `12`; crypto_alt avg `-0.5322` n `229`; crypto_major avg `-1.3766` n `8`; equity avg `-1.9175` n `90`; fx avg `-0.0148` n `6`; index avg `-0.3948` n `25`; metal avg `-0.334` n `20`; unknown avg `-0.6269` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
