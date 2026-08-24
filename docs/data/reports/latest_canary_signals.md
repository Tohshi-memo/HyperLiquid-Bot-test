# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T17:27:41.538607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7582` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.717` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7017` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6597` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.7988` n `231`; crypto_major avg `-0.8625` n `8`; equity avg `-0.1914` n `122`; fx avg `0.0023` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0571` n `20`; unknown avg `0.002` n `794`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `-1.5011` n `231`; crypto_major avg `-1.7612` n `8`; equity avg `-0.377` n `122`; fx avg `-0.0026` n `6`; index avg `-0.0442` n `25`; metal avg `-0.1015` n `20`; unknown avg `0.1649` n `793`
- 4h: commodity avg `-0.3288` n `12`; crypto_alt avg `-1.516` n `231`; crypto_major avg `-1.8604` n `8`; equity avg `-0.6194` n `122`; fx avg `-0.0277` n `6`; index avg `-0.1022` n `25`; metal avg `-0.1587` n `20`; unknown avg `0.5293` n `793`
- 24h: commodity avg `-0.2905` n `12`; crypto_alt avg `-1.7634` n `231`; crypto_major avg `-1.0876` n `8`; equity avg `-2.4118` n `122`; fx avg `-0.1403` n `6`; index avg `-0.306` n `25`; metal avg `0.1089` n `20`; unknown avg `3.3299` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
