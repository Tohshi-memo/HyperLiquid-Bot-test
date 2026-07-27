# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T14:52:30.771224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.5563` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3439` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.0831` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `0.2182` n `230`; crypto_major avg `0.2175` n `8`; equity avg `0.6488` n `102`; fx avg `-0.0073` n `6`; index avg `0.0471` n `25`; metal avg `0.0736` n `20`; unknown avg `0.2095` n `774`
- 1h: commodity avg `-0.079` n `12`; crypto_alt avg `-1.7016` n `230`; crypto_major avg `-1.699` n `8`; equity avg `-1.9802` n `102`; fx avg `-0.038` n `6`; index avg `-0.3551` n `25`; metal avg `-0.1427` n `20`; unknown avg `0.0335` n `774`
- 4h: commodity avg `0.1609` n `12`; crypto_alt avg `-1.7404` n `230`; crypto_major avg `-1.6373` n `8`; equity avg `-2.8171` n `102`; fx avg `-0.0445` n `6`; index avg `-0.5542` n `25`; metal avg `-0.2262` n `20`; unknown avg `-0.0542` n `774`
- 24h: commodity avg `-0.4286` n `12`; crypto_alt avg `-1.0103` n `230`; crypto_major avg `-0.3461` n `8`; equity avg `-1.6575` n `102`; fx avg `0.0478` n `6`; index avg `-0.4081` n `25`; metal avg `0.1516` n `20`; unknown avg `-0.2991` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
