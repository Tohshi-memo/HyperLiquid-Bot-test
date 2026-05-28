# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T06:22:17.119077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2095` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0767` n `12`; crypto_alt avg `-0.0089` n `228`; crypto_major avg `0.0012` n `8`; equity avg `0.1434` n `67`; fx avg `-0.0008` n `6`; index avg `0.0348` n `23`; metal avg `-0.0423` n `18`; unknown avg `-0.0259` n `419`
- 1h: commodity avg `-0.2352` n `12`; crypto_alt avg `0.3642` n `228`; crypto_major avg `0.2166` n `8`; equity avg `0.8106` n `67`; fx avg `0.0164` n `6`; index avg `0.3108` n `23`; metal avg `0.574` n `18`; unknown avg `0.157` n `409`
- 4h: commodity avg `0.4641` n `12`; crypto_alt avg `-2.7686` n `228`; crypto_major avg `-1.4767` n `8`; equity avg `-0.3756` n `67`; fx avg `-0.0746` n `6`; index avg `-0.2672` n `23`; metal avg `-0.3386` n `18`; unknown avg `-0.557` n `409`
- 24h: commodity avg `0.0857` n `12`; crypto_alt avg `-4.8854` n `228`; crypto_major avg `-3.627` n `8`; equity avg `-0.9494` n `67`; fx avg `-0.1345` n `6`; index avg `-0.865` n `23`; metal avg `-1.7712` n `18`; unknown avg `-1.9429` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
