# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T19:07:24.813810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0964` n `13`; crypto_alt avg `0.0577` n `239`; crypto_major avg `0.1589` n `8`; equity avg `0.1751` n `162`; fx avg `0.0027` n `6`; index avg `0.0226` n `27`; metal avg `-0.0022` n `20`; unknown avg `0.1116` n `1256`
- 1h: commodity avg `-0.0855` n `13`; crypto_alt avg `0.385` n `239`; crypto_major avg `0.409` n `8`; equity avg `0.6247` n `162`; fx avg `-0.0247` n `6`; index avg `0.074` n `27`; metal avg `-0.0104` n `20`; unknown avg `0.168` n `1260`
- 4h: commodity avg `-0.3134` n `13`; crypto_alt avg `-0.4127` n `239`; crypto_major avg `-0.3143` n `8`; equity avg `0.3234` n `162`; fx avg `-0.0915` n `6`; index avg `0.0343` n `27`; metal avg `-0.2166` n `20`; unknown avg `-0.871` n `1250`
- 24h: commodity avg `-0.1878` n `13`; crypto_alt avg `0.2366` n `239`; crypto_major avg `-1.1541` n `8`; equity avg `-2.318` n `162`; fx avg `-0.0544` n `6`; index avg `-0.1848` n `27`; metal avg `-0.2542` n `20`; unknown avg `1.9557` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
