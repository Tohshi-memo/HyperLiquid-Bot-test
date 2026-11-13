# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T22:37:29.707751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1279` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0181` n `13`; crypto_alt avg `0.2673` n `239`; crypto_major avg `0.0634` n `8`; equity avg `-0.0594` n `162`; fx avg `-0.008` n `6`; index avg `-0.0041` n `27`; metal avg `0.0052` n `20`; unknown avg `-0.059` n `1262`
- 1h: commodity avg `-0.1163` n `13`; crypto_alt avg `-0.3643` n `239`; crypto_major avg `-0.3559` n `8`; equity avg `-0.0645` n `162`; fx avg `0.0058` n `6`; index avg `0.0251` n `27`; metal avg `0.0802` n `20`; unknown avg `5.8576` n `1252`
- 4h: commodity avg `-0.0103` n `13`; crypto_alt avg `-1.0494` n `239`; crypto_major avg `-1.1188` n `8`; equity avg `-0.4739` n `162`; fx avg `-0.0087` n `6`; index avg `0.0091` n `27`; metal avg `-0.0899` n `20`; unknown avg `9.129` n `1210`
- 24h: commodity avg `-0.3488` n `13`; crypto_alt avg `-1.3945` n `239`; crypto_major avg `-2.5865` n `8`; equity avg `-3.1166` n `162`; fx avg `-0.0645` n `6`; index avg `-0.2216` n `27`; metal avg `-0.2963` n `20`; unknown avg `1.0819` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
