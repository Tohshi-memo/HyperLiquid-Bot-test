# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T00:37:27.206204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9023` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8024` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0443` n `12`; crypto_alt avg `0.0942` n `230`; crypto_major avg `0.0443` n `8`; equity avg `0.0998` n `102`; fx avg `-0.0219` n `6`; index avg `0.0178` n `25`; metal avg `0.0039` n `20`; unknown avg `0.3211` n `774`
- 1h: commodity avg `-0.0993` n `12`; crypto_alt avg `0.038` n `230`; crypto_major avg `-0.1686` n `8`; equity avg `-0.4564` n `102`; fx avg `0.0489` n `6`; index avg `-0.1712` n `25`; metal avg `-0.1011` n `20`; unknown avg `0.1816` n `774`
- 4h: commodity avg `-0.0503` n `12`; crypto_alt avg `-2.0127` n `230`; crypto_major avg `-2.0344` n `8`; equity avg `-0.9777` n `102`; fx avg `0.046` n `6`; index avg `-0.232` n `25`; metal avg `-0.1321` n `20`; unknown avg `1.4404` n `774`
- 24h: commodity avg `-0.711` n `12`; crypto_alt avg `-3.4925` n `230`; crypto_major avg `-2.8426` n `8`; equity avg `-2.1382` n `102`; fx avg `-0.0327` n `6`; index avg `-0.5939` n `25`; metal avg `-0.1915` n `20`; unknown avg `1161.8094` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3358`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2981`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
