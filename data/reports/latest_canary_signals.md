# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T10:37:23.465171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.158` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0393` n `12`; crypto_alt avg `0.0519` n `228`; crypto_major avg `-0.021` n `8`; equity avg `-0.0019` n `74`; fx avg `0.0057` n `6`; index avg `-0.0328` n `23`; metal avg `0.0809` n `18`; unknown avg `-0.0147` n `547`
- 1h: commodity avg `0.219` n `12`; crypto_alt avg `0.0806` n `228`; crypto_major avg `-0.0179` n `8`; equity avg `-0.0678` n `74`; fx avg `0.0591` n `6`; index avg `-0.0004` n `23`; metal avg `0.2655` n `18`; unknown avg `0.9549` n `547`
- 4h: commodity avg `-0.0388` n `12`; crypto_alt avg `-0.8546` n `228`; crypto_major avg `-0.9924` n `8`; equity avg `-0.1965` n `74`; fx avg `0.1933` n `6`; index avg `0.1656` n `23`; metal avg `0.4143` n `18`; unknown avg `0.1836` n `547`
- 24h: commodity avg `-1.1091` n `12`; crypto_alt avg `-0.9334` n `228`; crypto_major avg `-0.0141` n `8`; equity avg `2.112` n `74`; fx avg `0.0822` n `6`; index avg `1.0653` n `23`; metal avg `0.9734` n `18`; unknown avg `-2.8366` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
