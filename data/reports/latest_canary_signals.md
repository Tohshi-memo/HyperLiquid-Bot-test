# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T16:22:34.339700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.749` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3679` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0792` n `12`; crypto_alt avg `-0.3923` n `233`; crypto_major avg `-0.3249` n `8`; equity avg `-0.2587` n `134`; fx avg `0.0194` n `6`; index avg `-0.0377` n `26`; metal avg `-0.0515` n `20`; unknown avg `6.8089` n `797`
- 1h: commodity avg `-0.0836` n `12`; crypto_alt avg `0.0286` n `233`; crypto_major avg `0.1274` n `8`; equity avg `-0.1075` n `134`; fx avg `-0.0025` n `6`; index avg `-0.0373` n `26`; metal avg `0.1031` n `20`; unknown avg `0.2211` n `795`
- 4h: commodity avg `0.0082` n `12`; crypto_alt avg `-1.5739` n `233`; crypto_major avg `-1.412` n `8`; equity avg `-0.0003` n `134`; fx avg `0.0145` n `6`; index avg `-0.0441` n `26`; metal avg `0.337` n `20`; unknown avg `8.8892` n `766`
- 24h: commodity avg `0.5214` n `12`; crypto_alt avg `-1.73` n `233`; crypto_major avg `-0.612` n `8`; equity avg `-0.7243` n `134`; fx avg `-0.0985` n `6`; index avg `-0.2585` n `26`; metal avg `0.2969` n `20`; unknown avg `7.2256` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
