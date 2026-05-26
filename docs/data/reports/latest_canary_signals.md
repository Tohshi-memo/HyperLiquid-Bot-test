# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T17:07:18.691251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2012` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1073` n `12`; crypto_alt avg `-0.0789` n `228`; crypto_major avg `-0.0763` n `8`; equity avg `0.149` n `67`; fx avg `-0.0006` n `6`; index avg `0.0041` n `23`; metal avg `-0.0094` n `18`; unknown avg `-0.0916` n `418`
- 1h: commodity avg `-0.1192` n `12`; crypto_alt avg `-0.0607` n `228`; crypto_major avg `-0.1161` n `8`; equity avg `0.2235` n `67`; fx avg `0.0261` n `6`; index avg `0.0721` n `23`; metal avg `0.0361` n `18`; unknown avg `0.2128` n `418`
- 4h: commodity avg `0.0764` n `12`; crypto_alt avg `-1.0124` n `228`; crypto_major avg `-0.8446` n `8`; equity avg `0.1612` n `67`; fx avg `-0.0058` n `6`; index avg `0.3566` n `23`; metal avg `-0.2351` n `18`; unknown avg `0.8744` n `416`
- 24h: commodity avg `1.4117` n `12`; crypto_alt avg `-1.6277` n `228`; crypto_major avg `-1.2876` n `8`; equity avg `-0.3236` n `67`; fx avg `-0.1096` n `6`; index avg `0.4385` n `23`; metal avg `-1.4019` n `18`; unknown avg `0.197` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
