# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T23:37:24.477189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9374` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.6778` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.672` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8937` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2637` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-1.4375` n `231`; crypto_major avg `-1.1249` n `8`; equity avg `-0.1498` n `128`; fx avg `0.0089` n `6`; index avg `-0.0378` n `26`; metal avg `-0.0623` n `20`; unknown avg `0.9368` n `793`
- 1h: commodity avg `-0.0627` n `12`; crypto_alt avg `-1.7132` n `231`; crypto_major avg `-1.3697` n `8`; equity avg `-0.5862` n `128`; fx avg `0.0112` n `6`; index avg `-0.106` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.1373` n `791`
- 4h: commodity avg `0.0561` n `12`; crypto_alt avg `-2.8957` n `231`; crypto_major avg `-2.8813` n `8`; equity avg `-0.9876` n `128`; fx avg `0.0134` n `6`; index avg `-0.2093` n `26`; metal avg `-0.2035` n `20`; unknown avg `2.0025` n `791`
- 24h: commodity avg `0.2647` n `12`; crypto_alt avg `-1.3639` n `231`; crypto_major avg `-2.1715` n `8`; equity avg `-0.8486` n `128`; fx avg `0.0384` n `6`; index avg `-0.183` n `26`; metal avg `-0.1054` n `20`; unknown avg `-0.3433` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
