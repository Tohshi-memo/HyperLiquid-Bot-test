# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T18:07:33.867249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `13`; crypto_alt avg `-0.2784` n `237`; crypto_major avg `-0.1925` n `8`; equity avg `-0.0628` n `151`; fx avg `0.0021` n `6`; index avg `-0.0116` n `26`; metal avg `-0.0011` n `20`; unknown avg `22.6659` n `1195`
- 1h: commodity avg `-0.0223` n `13`; crypto_alt avg `-0.3022` n `237`; crypto_major avg `-0.1934` n `8`; equity avg `0.0609` n `151`; fx avg `0.0124` n `6`; index avg `0.0393` n `26`; metal avg `0.0557` n `20`; unknown avg `6.1104` n `1187`
- 4h: commodity avg `-0.1083` n `13`; crypto_alt avg `0.297` n `237`; crypto_major avg `-0.2141` n `8`; equity avg `0.5689` n `151`; fx avg `-0.0181` n `6`; index avg `0.0875` n `26`; metal avg `0.0605` n `20`; unknown avg `2.3994` n `1180`
- 24h: commodity avg `-0.473` n `13`; crypto_alt avg `2.6569` n `237`; crypto_major avg `1.4731` n `8`; equity avg `0.338` n `151`; fx avg `0.0217` n `6`; index avg `0.0456` n `26`; metal avg `-0.0165` n `20`; unknown avg `3.8572` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
