# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T23:07:26.307829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7111` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7025` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3212` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.2529` n `230`; crypto_major avg `-0.2815` n `8`; equity avg `-0.1757` n `102`; fx avg `0.0034` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.0164` n `774`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `-1.57` n `230`; crypto_major avg `-1.3477` n `8`; equity avg `-0.4671` n `102`; fx avg `-0.0023` n `6`; index avg `-0.0265` n `25`; metal avg `-0.0475` n `20`; unknown avg `1.1677` n `774`
- 4h: commodity avg `-0.0378` n `12`; crypto_alt avg `-1.7502` n `230`; crypto_major avg `-1.7422` n `8`; equity avg `-0.4101` n `102`; fx avg `-0.02` n `6`; index avg `-0.0311` n `25`; metal avg `-0.0397` n `20`; unknown avg `1136.5579` n `774`
- 24h: commodity avg `-0.715` n `12`; crypto_alt avg `-3.7173` n `230`; crypto_major avg `-3.1838` n `8`; equity avg `-2.1057` n `102`; fx avg `-0.0341` n `6`; index avg `-0.5139` n `25`; metal avg `-0.0094` n `20`; unknown avg `1161.759` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2769`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
