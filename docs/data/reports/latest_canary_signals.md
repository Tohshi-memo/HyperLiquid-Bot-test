# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T00:37:22.140654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0815` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0544` n `12`; crypto_alt avg `-0.184` n `228`; crypto_major avg `0.0219` n `8`; equity avg `0.02` n `67`; fx avg `0.0101` n `6`; index avg `-0.0152` n `23`; metal avg `-0.0551` n `18`; unknown avg `-0.0441` n `419`
- 1h: commodity avg `0.2411` n `12`; crypto_alt avg `0.3141` n `228`; crypto_major avg `0.3853` n `8`; equity avg `-0.2476` n `67`; fx avg `0.0436` n `6`; index avg `-0.1318` n `23`; metal avg `0.0274` n `18`; unknown avg `0.0671` n `419`
- 4h: commodity avg `0.4149` n `12`; crypto_alt avg `-1.8093` n `228`; crypto_major avg `-1.3503` n `8`; equity avg `-0.6394` n `67`; fx avg `0.0146` n `6`; index avg `-0.2688` n `23`; metal avg `-0.0073` n `18`; unknown avg `0.6547` n `419`
- 24h: commodity avg `-0.7748` n `12`; crypto_alt avg `-2.5567` n `228`; crypto_major avg `-1.6311` n `8`; equity avg `-0.7836` n `67`; fx avg `-0.0581` n `6`; index avg `-0.8593` n `23`; metal avg `-1.6504` n `18`; unknown avg `-1.0782` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
