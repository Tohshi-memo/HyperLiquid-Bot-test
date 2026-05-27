# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T23:54:15.254690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3421` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1296` n `12`; crypto_alt avg `0.344` n `228`; crypto_major avg `0.2173` n `8`; equity avg `-0.1749` n `67`; fx avg `0.009` n `6`; index avg `-0.0747` n `23`; metal avg `-0.1505` n `18`; unknown avg `0.0193` n `419`
- 1h: commodity avg `0.2876` n `12`; crypto_alt avg `-0.0426` n `228`; crypto_major avg `-0.3171` n `8`; equity avg `-0.3039` n `67`; fx avg `-0.0064` n `6`; index avg `-0.1547` n `23`; metal avg `-0.2264` n `18`; unknown avg `1.4275` n `419`
- 4h: commodity avg `0.2649` n `12`; crypto_alt avg `-1.9174` n `228`; crypto_major avg `-1.4609` n `8`; equity avg `-0.4273` n `67`; fx avg `-0.0173` n `6`; index avg `-0.1188` n `23`; metal avg `-0.1736` n `18`; unknown avg `0.0733` n `419`
- 24h: commodity avg `-0.794` n `12`; crypto_alt avg `-1.9708` n `228`; crypto_major avg `-1.4743` n `8`; equity avg `-0.7183` n `67`; fx avg `-0.1128` n `6`; index avg `-0.7702` n `23`; metal avg `-1.7996` n `18`; unknown avg `-0.6123` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
