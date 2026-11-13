# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T22:07:24.743896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0155` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0598` n `13`; crypto_alt avg `-0.2981` n `239`; crypto_major avg `-0.4179` n `8`; equity avg `-0.094` n `162`; fx avg `-0.0068` n `6`; index avg `-0.0121` n `27`; metal avg `0.0136` n `20`; unknown avg `0.2008` n `1250`
- 1h: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.5664` n `239`; crypto_major avg `-0.8963` n `8`; equity avg `-0.2659` n `162`; fx avg `-0.0227` n `6`; index avg `0.002` n `27`; metal avg `0.023` n `20`; unknown avg `0.4287` n `1252`
- 4h: commodity avg `0.0166` n `13`; crypto_alt avg `-0.7133` n `239`; crypto_major avg `-0.962` n `8`; equity avg `0.0082` n `162`; fx avg `-0.0422` n `6`; index avg `0.0535` n `27`; metal avg `-0.0777` n `20`; unknown avg `2.9188` n `1210`
- 24h: commodity avg `-0.2923` n `13`; crypto_alt avg `-1.5282` n `239`; crypto_major avg `-2.8627` n `8`; equity avg `-3.0481` n `162`; fx avg `-0.0772` n `6`; index avg `-0.2172` n `27`; metal avg `-0.2948` n `20`; unknown avg `6.5935` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
