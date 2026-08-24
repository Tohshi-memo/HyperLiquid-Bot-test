# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T02:07:20.184400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6447` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4766` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.4101` n `231`; crypto_major avg `-0.22` n `8`; equity avg `-0.3603` n `122`; fx avg `-0.0213` n `6`; index avg `-0.0694` n `25`; metal avg `0.0699` n `20`; unknown avg `0.995` n `793`
- 1h: commodity avg `-0.0161` n `12`; crypto_alt avg `-1.4586` n `231`; crypto_major avg `-1.0799` n `8`; equity avg `-0.9121` n `122`; fx avg `-0.0223` n `6`; index avg `-0.1096` n `25`; metal avg `0.0053` n `20`; unknown avg `0.658` n `793`
- 4h: commodity avg `-0.2432` n `12`; crypto_alt avg `-2.4731` n `231`; crypto_major avg `-1.5842` n `8`; equity avg `-1.1097` n `122`; fx avg `-0.0555` n `6`; index avg `-0.1076` n `25`; metal avg `0.0605` n `20`; unknown avg `0.7147` n `793`
- 24h: commodity avg `-0.4064` n `12`; crypto_alt avg `1.5267` n `231`; crypto_major avg `-0.5218` n `8`; equity avg `-0.638` n `122`; fx avg `-0.1871` n `6`; index avg `-0.0528` n `25`; metal avg `0.099` n `20`; unknown avg `6.0305` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
