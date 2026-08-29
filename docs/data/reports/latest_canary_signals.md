# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T22:52:29.072013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.0559` n `231`; crypto_major avg `0.0454` n `8`; equity avg `-0.0133` n `128`; fx avg `0.0036` n `6`; index avg `0.0234` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.0549` n `793`
- 1h: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.014` n `231`; crypto_major avg `0.0812` n `8`; equity avg `0.0101` n `128`; fx avg `0.0005` n `6`; index avg `0.0263` n `26`; metal avg `-0.0083` n `20`; unknown avg `0.0431` n `774`
- 4h: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0778` n `231`; crypto_major avg `-0.0512` n `8`; equity avg `0.1688` n `128`; fx avg `-0.011` n `6`; index avg `0.059` n `26`; metal avg `0.0025` n `20`; unknown avg `0.196` n `774`
- 24h: commodity avg `0.0222` n `12`; crypto_alt avg `0.4994` n `231`; crypto_major avg `0.8216` n `8`; equity avg `0.4249` n `128`; fx avg `-0.0292` n `6`; index avg `0.1095` n `26`; metal avg `0.1077` n `20`; unknown avg `0.0121` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
