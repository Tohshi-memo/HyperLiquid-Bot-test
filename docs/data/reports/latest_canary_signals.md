# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T19:07:42.523094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.2535` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8927` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5257` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `-0.3091` n `231`; crypto_major avg `-0.1367` n `8`; equity avg `-0.1387` n `122`; fx avg `0.0019` n `6`; index avg `-0.0116` n `25`; metal avg `0.0143` n `20`; unknown avg `1.442` n `794`
- 1h: commodity avg `0.0878` n `12`; crypto_alt avg `-0.5837` n `231`; crypto_major avg `-0.3626` n `8`; equity avg `-0.0692` n `122`; fx avg `0.0043` n `6`; index avg `0.0117` n `25`; metal avg `0.0226` n `20`; unknown avg `1.0147` n `794`
- 4h: commodity avg `0.0105` n `12`; crypto_alt avg `-1.6561` n `231`; crypto_major avg `-1.7883` n `8`; equity avg `0.4652` n `122`; fx avg `-0.0336` n `6`; index avg `0.1044` n `25`; metal avg `-0.2626` n `20`; unknown avg `0.0527` n `793`
- 24h: commodity avg `-0.1351` n `12`; crypto_alt avg `-1.8405` n `231`; crypto_major avg `-0.9118` n `8`; equity avg `-2.5415` n `122`; fx avg `-0.1368` n `6`; index avg `-0.321` n `25`; metal avg `0.0508` n `20`; unknown avg `2.4674` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
