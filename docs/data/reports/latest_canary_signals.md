# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T05:37:27.415017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.9397` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8902` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7402` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0154` n `13`; crypto_alt avg `-0.2588` n `239`; crypto_major avg `-0.2518` n `8`; equity avg `-0.0175` n `162`; fx avg `0.0` n `6`; index avg `0.0029` n `27`; metal avg `-0.0063` n `20`; unknown avg `9.5393` n `1262`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `-0.0048` n `239`; crypto_major avg `0.0049` n `8`; equity avg `0.0399` n `162`; fx avg `-0.0032` n `6`; index avg `0.0096` n `27`; metal avg `-0.0003` n `20`; unknown avg `2.9241` n `1252`
- 4h: commodity avg `-0.0427` n `13`; crypto_alt avg `-1.2461` n `239`; crypto_major avg `-1.9632` n `8`; equity avg `-0.223` n `162`; fx avg `-0.0094` n `6`; index avg `-0.0235` n `27`; metal avg `-0.073` n `20`; unknown avg `9.0654` n `1240`
- 24h: commodity avg `-0.0926` n `13`; crypto_alt avg `-0.243` n `239`; crypto_major avg `-1.8164` n `8`; equity avg `-2.4879` n `162`; fx avg `-0.111` n `6`; index avg `-0.1967` n `27`; metal avg `-0.5825` n `20`; unknown avg `66.082` n `1024`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
