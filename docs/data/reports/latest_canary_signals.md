# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T04:22:26.427831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4238` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3937` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3582` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1072` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.1436` n `239`; crypto_major avg `0.1688` n `8`; equity avg `0.0375` n `162`; fx avg `0.0061` n `6`; index avg `0.0036` n `27`; metal avg `0.0121` n `20`; unknown avg `3.1396` n `1260`
- 1h: commodity avg `-0.0435` n `13`; crypto_alt avg `-0.5042` n `239`; crypto_major avg `-0.7976` n `8`; equity avg `-0.0778` n `162`; fx avg `0.0079` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0341` n `20`; unknown avg `199.3923` n `1250`
- 4h: commodity avg `-0.0067` n `13`; crypto_alt avg `-1.5428` n `239`; crypto_major avg `-2.4305` n `8`; equity avg `-0.3233` n `162`; fx avg `-0.0115` n `6`; index avg `-0.0368` n `27`; metal avg `-0.0723` n `20`; unknown avg `8.0788` n `1250`
- 24h: commodity avg `-0.1673` n `13`; crypto_alt avg `-0.5801` n `239`; crypto_major avg `-2.2597` n `8`; equity avg `-2.8066` n `162`; fx avg `-0.0884` n `6`; index avg `-0.2326` n `27`; metal avg `-0.6032` n `20`; unknown avg `64.5249` n `1032`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
