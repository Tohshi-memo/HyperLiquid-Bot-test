# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T21:07:33.554557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9025` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.8868` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8701` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.5824` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5096` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.6869` n `231`; crypto_major avg `-0.6123` n `8`; equity avg `-0.0816` n `122`; fx avg `-0.005` n `6`; index avg `-0.0072` n `25`; metal avg `-0.041` n `20`; unknown avg `-0.1524` n `795`
- 1h: commodity avg `0.065` n `12`; crypto_alt avg `-1.6221` n `231`; crypto_major avg `-1.5851` n `8`; equity avg `-0.1915` n `122`; fx avg `-0.0141` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0755` n `20`; unknown avg `-0.3705` n `795`
- 4h: commodity avg `-0.154` n `12`; crypto_alt avg `-2.2045` n `231`; crypto_major avg `-1.8199` n `8`; equity avg `0.0826` n `122`; fx avg `-0.0087` n `6`; index avg `0.0502` n `25`; metal avg `0.0669` n `20`; unknown avg `-0.5046` n `795`
- 24h: commodity avg `-0.6997` n `12`; crypto_alt avg `-3.1375` n `231`; crypto_major avg `-1.6813` n `8`; equity avg `1.8466` n `122`; fx avg `0.0433` n `6`; index avg `0.2559` n `25`; metal avg `-0.0707` n `20`; unknown avg `-0.7265` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
