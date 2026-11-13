# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T22:22:31.876821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1677` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0117` n `13`; crypto_alt avg `-0.31` n `239`; crypto_major avg `0.0094` n `8`; equity avg `-0.0487` n `162`; fx avg `0.0152` n `6`; index avg `-0.0074` n `27`; metal avg `-0.0077` n `20`; unknown avg `0.1036` n `1260`
- 1h: commodity avg `-0.0523` n `13`; crypto_alt avg `-0.6755` n `239`; crypto_major avg `-0.3764` n `8`; equity avg `-0.1298` n `162`; fx avg `0.0033` n `6`; index avg `0.0186` n `27`; metal avg `-0.0228` n `20`; unknown avg `5.112` n `1252`
- 4h: commodity avg `0.0646` n `13`; crypto_alt avg `-1.1809` n `239`; crypto_major avg `-1.1245` n `8`; equity avg `-0.15` n `162`; fx avg `0.0016` n `6`; index avg `0.0432` n `27`; metal avg `-0.1186` n `20`; unknown avg `4.1522` n `1210`
- 24h: commodity avg `-0.3018` n `13`; crypto_alt avg `-1.6749` n `239`; crypto_major avg `-2.7311` n `8`; equity avg `-2.9683` n `162`; fx avg `-0.0594` n `6`; index avg `-0.2069` n `27`; metal avg `-0.2908` n `20`; unknown avg `1.6878` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
