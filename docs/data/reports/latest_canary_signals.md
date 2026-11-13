# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T23:22:28.274824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7231` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7199` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.0397` n `239`; crypto_major avg `-0.1507` n `8`; equity avg `-0.0425` n `162`; fx avg `-0.0074` n `6`; index avg `0.0003` n `27`; metal avg `0.004` n `20`; unknown avg `4.7175` n `1260`
- 1h: commodity avg `-0.0118` n `13`; crypto_alt avg `-0.0179` n `239`; crypto_major avg `-0.458` n `8`; equity avg `-0.3017` n `162`; fx avg `-0.0085` n `6`; index avg `-0.0215` n `27`; metal avg `-0.0098` n `20`; unknown avg `0.2736` n `1212`
- 4h: commodity avg `0.079` n `13`; crypto_alt avg `-1.4634` n `239`; crypto_major avg `-1.7885` n `8`; equity avg `-1.0727` n `162`; fx avg `-0.0126` n `6`; index avg `-0.0686` n `27`; metal avg `-0.0654` n `20`; unknown avg `3.7537` n `1162`
- 24h: commodity avg `-0.3303` n `13`; crypto_alt avg `-1.8296` n `239`; crypto_major avg `-3.3132` n `8`; equity avg `-3.6933` n `162`; fx avg `-0.0732` n `6`; index avg `-0.2878` n `27`; metal avg `-0.3225` n `20`; unknown avg `64.0426` n `1035`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
