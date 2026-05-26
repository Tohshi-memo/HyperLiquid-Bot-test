# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T19:07:20.578487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5542` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5455` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0715` n `12`; crypto_alt avg `-0.1329` n `228`; crypto_major avg `-0.2993` n `8`; equity avg `-0.1143` n `67`; fx avg `0.0108` n `6`; index avg `-0.0702` n `23`; metal avg `0.0608` n `18`; unknown avg `0.2614` n `418`
- 1h: commodity avg `-0.2462` n `12`; crypto_alt avg `-0.2452` n `228`; crypto_major avg `-0.3303` n `8`; equity avg `-0.0823` n `67`; fx avg `0.0123` n `6`; index avg `0.0403` n `23`; metal avg `0.4025` n `18`; unknown avg `-0.055` n `418`
- 4h: commodity avg `-0.5818` n `12`; crypto_alt avg `-1.6276` n `228`; crypto_major avg `-1.4717` n `8`; equity avg `-0.0395` n `67`; fx avg `0.0383` n `6`; index avg `0.0825` n `23`; metal avg `0.0738` n `18`; unknown avg `1.478` n `418`
- 24h: commodity avg `0.8672` n `12`; crypto_alt avg `-2.4938` n `228`; crypto_major avg `-1.7758` n `8`; equity avg `-0.4824` n `67`; fx avg `-0.1116` n `6`; index avg `0.4004` n `23`; metal avg `-1.1678` n `18`; unknown avg `0.8756` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
