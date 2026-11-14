# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T06:07:34.962978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1621` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `0.1372` n `239`; crypto_major avg `0.3259` n `8`; equity avg `0.1007` n `162`; fx avg `0.0013` n `6`; index avg `0.009` n `27`; metal avg `0.016` n `20`; unknown avg `0.7424` n `1236`
- 1h: commodity avg `-0.0046` n `13`; crypto_alt avg `0.5502` n `239`; crypto_major avg `0.5362` n `8`; equity avg `0.208` n `162`; fx avg `0.0026` n `6`; index avg `0.02` n `27`; metal avg `0.0255` n `20`; unknown avg `0.3646` n `1234`
- 4h: commodity avg `-0.0539` n `13`; crypto_alt avg `-0.5359` n `239`; crypto_major avg `-1.1726` n `8`; equity avg `-0.0433` n `162`; fx avg `0.0077` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0419` n `20`; unknown avg `0.565` n `1218`
- 24h: commodity avg `-0.1838` n `13`; crypto_alt avg `-0.2069` n `239`; crypto_major avg `-1.3346` n `8`; equity avg `-2.1579` n `162`; fx avg `-0.1224` n `6`; index avg `-0.1712` n `27`; metal avg `-0.4207` n `20`; unknown avg `60.4442` n `1022`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
