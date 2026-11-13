# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T11:22:37.867062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `13`; crypto_alt avg `0.0265` n `239`; crypto_major avg `0.136` n `8`; equity avg `0.0182` n `162`; fx avg `0.0101` n `6`; index avg `-0.0043` n `27`; metal avg `0.0248` n `20`; unknown avg `-0.1333` n `1258`
- 1h: commodity avg `0.0613` n `13`; crypto_alt avg `0.1173` n `239`; crypto_major avg `0.2565` n `8`; equity avg `0.3224` n `162`; fx avg `-0.0039` n `6`; index avg `0.033` n `27`; metal avg `-0.0153` n `20`; unknown avg `41.1416` n `1238`
- 4h: commodity avg `-0.0181` n `13`; crypto_alt avg `-0.2533` n `239`; crypto_major avg `0.4673` n `8`; equity avg `0.4229` n `162`; fx avg `-0.0202` n `6`; index avg `0.047` n `27`; metal avg `-0.0713` n `20`; unknown avg `44.9508` n `1148`
- 24h: commodity avg `0.7557` n `13`; crypto_alt avg `-0.7692` n `239`; crypto_major avg `-2.3746` n `8`; equity avg `-0.7242` n `162`; fx avg `-0.0338` n `6`; index avg `0.0631` n `27`; metal avg `-0.4151` n `20`; unknown avg `1.597` n `1075`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
