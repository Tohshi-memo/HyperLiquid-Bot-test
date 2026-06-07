# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T13:52:22.575943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `75.16` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.3511` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.2049` n `228`; crypto_major avg `0.2291` n `8`; equity avg `0.1791` n `74`; fx avg `-0.0095` n `6`; index avg `0.1142` n `23`; metal avg `0.0389` n `18`; unknown avg `0.0355` n `516`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `0.2981` n `228`; crypto_major avg `0.102` n `8`; equity avg `0.1552` n `74`; fx avg `0.0047` n `6`; index avg `0.1139` n `23`; metal avg `0.0137` n `18`; unknown avg `0.1024` n `516`
- 4h: commodity avg `0.2176` n `12`; crypto_alt avg `-1.237` n `228`; crypto_major avg `-1.2831` n `8`; equity avg `-0.1056` n `74`; fx avg `0.0135` n `6`; index avg `0.068` n `23`; metal avg `-0.2869` n `18`; unknown avg `-3.2537` n `516`
- 24h: commodity avg `0.1483` n `12`; crypto_alt avg `1.7695` n `228`; crypto_major avg `1.8071` n `8`; equity avg `1.5769` n `74`; fx avg `0.0297` n `6`; index avg `0.3979` n `23`; metal avg `0.3677` n `18`; unknown avg `5.5471` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
