# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T02:37:36.534620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5535` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5323` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3826` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.0153` n `239`; crypto_major avg `-0.2556` n `8`; equity avg `-0.0256` n `162`; fx avg `0.0002` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0352` n `20`; unknown avg `-0.0216` n `1262`
- 1h: commodity avg `-0.0192` n `13`; crypto_alt avg `-1.1568` n `239`; crypto_major avg `-1.4029` n `8`; equity avg `-0.2369` n `162`; fx avg `-0.0063` n `6`; index avg `-0.0203` n `27`; metal avg `-0.0752` n `20`; unknown avg `8.2141` n `1256`
- 4h: commodity avg `0.0726` n `13`; crypto_alt avg `-1.218` n `239`; crypto_major avg `-1.5957` n `8`; equity avg `-0.4424` n `162`; fx avg `-0.03` n `6`; index avg `-0.0422` n `27`; metal avg `-0.0634` n `20`; unknown avg `0.2973` n `1206`
- 24h: commodity avg `-0.22` n `13`; crypto_alt avg `-2.1901` n `239`; crypto_major avg `-3.6022` n `8`; equity avg `-3.9791` n `162`; fx avg `-0.097` n `6`; index avg `-0.3767` n `27`; metal avg `-0.6651` n `20`; unknown avg `59.5366` n `1036`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
