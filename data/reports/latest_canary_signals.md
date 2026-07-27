# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T15:09:51.750600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5354` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2307` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1613` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0834` n `12`; crypto_alt avg `-0.1096` n `230`; crypto_major avg `-0.0965` n `8`; equity avg `-0.067` n `102`; fx avg `-0.0144` n `6`; index avg `0.0306` n `25`; metal avg `0.0544` n `20`; unknown avg `-0.0235` n `774`
- 1h: commodity avg `-0.1511` n `12`; crypto_alt avg `-1.5203` n `230`; crypto_major avg `-1.3869` n `8`; equity avg `-1.0141` n `102`; fx avg `-0.0392` n `6`; index avg `-0.1562` n `25`; metal avg `0.0262` n `20`; unknown avg `-0.1224` n `774`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `-1.7709` n `230`; crypto_major avg `-1.6677` n `8`; equity avg `-2.7481` n `102`; fx avg `-0.0524` n `6`; index avg `-0.5064` n `25`; metal avg `-0.1323` n `20`; unknown avg `-0.034` n `774`
- 24h: commodity avg `-0.5436` n `12`; crypto_alt avg `-1.1221` n `230`; crypto_major avg `-0.5791` n `8`; equity avg `-1.7336` n `102`; fx avg `0.0371` n `6`; index avg `-0.3812` n `25`; metal avg `0.2179` n `20`; unknown avg `-0.2754` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
