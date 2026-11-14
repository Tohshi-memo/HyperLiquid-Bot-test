# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T02:52:34.270365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2059` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0284` n `13`; crypto_alt avg `0.394` n `239`; crypto_major avg `0.4861` n `8`; equity avg `0.0742` n `162`; fx avg `0.0074` n `6`; index avg `0.0028` n `27`; metal avg `0.0172` n `20`; unknown avg `1.16` n `1262`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `-0.6163` n `239`; crypto_major avg `-0.8339` n `8`; equity avg `-0.132` n `162`; fx avg `-0.001` n `6`; index avg `-0.0189` n `27`; metal avg `-0.0563` n `20`; unknown avg `6.7889` n `1258`
- 4h: commodity avg `0.1014` n `13`; crypto_alt avg `-0.9465` n `239`; crypto_major avg `-1.2347` n `8`; equity avg `-0.2987` n `162`; fx avg `-0.0178` n `6`; index avg `-0.0288` n `27`; metal avg `-0.0417` n `20`; unknown avg `42.8637` n `1252`
- 24h: commodity avg `-0.1076` n `13`; crypto_alt avg `-1.1337` n `239`; crypto_major avg `-2.4751` n `8`; equity avg `-3.5162` n `162`; fx avg `-0.0725` n `6`; index avg `-0.3288` n `27`; metal avg `-0.6064` n `20`; unknown avg `59.4591` n `1036`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
