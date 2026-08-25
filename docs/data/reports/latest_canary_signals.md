# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T21:21:39.415698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8487` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8178` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7808` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5287` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `0.1382` n `231`; crypto_major avg `0.1099` n `8`; equity avg `0.0591` n `122`; fx avg `0.0` n `6`; index avg `0.0053` n `25`; metal avg `-0.0194` n `20`; unknown avg `0.2181` n `795`
- 1h: commodity avg `0.2121` n `12`; crypto_alt avg `-1.5188` n `231`; crypto_major avg `-1.5326` n `8`; equity avg `-0.1766` n `122`; fx avg `-0.0148` n `6`; index avg `-0.0039` n `25`; metal avg `-0.1093` n `20`; unknown avg `-0.3127` n `795`
- 4h: commodity avg `-0.1318` n `12`; crypto_alt avg `-1.988` n `231`; crypto_major avg `-1.7601` n `8`; equity avg `0.0886` n `122`; fx avg `-0.0168` n `6`; index avg `0.0577` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.335` n `795`
- 24h: commodity avg `-0.6858` n `12`; crypto_alt avg `-2.9581` n `231`; crypto_major avg `-1.5989` n `8`; equity avg `1.8827` n `122`; fx avg `0.0581` n `6`; index avg `0.2602` n `25`; metal avg `-0.0914` n `20`; unknown avg `-0.5663` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
