# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T11:52:39.670154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8442` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8096` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6322` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.092` n `230`; crypto_major avg `-0.1031` n `8`; equity avg `0.0261` n `121`; fx avg `-0.0021` n `6`; index avg `-0.0022` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.0079` n `794`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `0.4504` n `230`; crypto_major avg `0.2599` n `8`; equity avg `0.0197` n `121`; fx avg `0.006` n `6`; index avg `0.0132` n `25`; metal avg `0.0204` n `20`; unknown avg `0.2359` n `794`
- 4h: commodity avg `-0.0434` n `12`; crypto_alt avg `-1.446` n `230`; crypto_major avg `-1.8217` n `8`; equity avg `-0.1895` n `121`; fx avg `0.0358` n `6`; index avg `-0.0121` n `25`; metal avg `0.0225` n `20`; unknown avg `0.1113` n `794`
- 24h: commodity avg `0.0223` n `12`; crypto_alt avg `1.9276` n `230`; crypto_major avg `3.741` n `8`; equity avg `-0.9597` n `121`; fx avg `0.0787` n `6`; index avg `-0.112` n `23`; metal avg `-0.1972` n `18`; unknown avg `1.4746` n `758`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
