# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T18:52:18.673053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5593` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3214` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0787` n `12`; crypto_alt avg `-0.2795` n `228`; crypto_major avg `-0.2631` n `8`; equity avg `-0.0161` n `74`; fx avg `-0.0844` n `6`; index avg `-0.063` n `23`; metal avg `-0.0088` n `18`; unknown avg `0.1354` n `515`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.1426` n `228`; crypto_major avg `-0.114` n `8`; equity avg `0.0593` n `74`; fx avg `-0.0517` n `6`; index avg `-0.0741` n `23`; metal avg `0.0046` n `18`; unknown avg `0.1254` n `515`
- 4h: commodity avg `0.1122` n `12`; crypto_alt avg `-1.2385` n `228`; crypto_major avg `-1.4463` n `8`; equity avg `-0.2085` n `74`; fx avg `0.1229` n `6`; index avg `-0.1249` n `23`; metal avg `0.113` n `18`; unknown avg `-3.726` n `515`
- 24h: commodity avg `0.3192` n `12`; crypto_alt avg `0.2714` n `228`; crypto_major avg `0.3841` n `8`; equity avg `-0.7168` n `74`; fx avg `0.0936` n `6`; index avg `-0.2317` n `23`; metal avg `-0.5585` n `18`; unknown avg `-0.1823` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
