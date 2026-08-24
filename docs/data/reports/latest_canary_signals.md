# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T17:22:27.411308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8114` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.7698` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7011` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6586` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.8268` n `231`; crypto_major avg `-0.911` n `8`; equity avg `-0.2271` n `122`; fx avg `0.007` n `6`; index avg `-0.0141` n `25`; metal avg `-0.1064` n `20`; unknown avg `0.089` n `794`
- 1h: commodity avg `-0.0851` n `12`; crypto_alt avg `-1.5294` n `231`; crypto_major avg `-1.8093` n `8`; equity avg `-0.4125` n `122`; fx avg `0.002` n `6`; index avg `-0.0395` n `25`; metal avg `-0.1507` n `20`; unknown avg `0.2735` n `793`
- 4h: commodity avg `-0.3508` n `12`; crypto_alt avg `-1.5458` n `231`; crypto_major avg `-1.9089` n `8`; equity avg `-0.6552` n `122`; fx avg `-0.0231` n `6`; index avg `-0.0975` n `25`; metal avg `-0.2078` n `20`; unknown avg `0.5878` n `793`
- 24h: commodity avg `-0.3126` n `12`; crypto_alt avg `-1.7926` n `231`; crypto_major avg `-1.1373` n `8`; equity avg `-2.4479` n `122`; fx avg `-0.1357` n `6`; index avg `-0.3014` n `25`; metal avg `0.0595` n `20`; unknown avg `3.3351` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
