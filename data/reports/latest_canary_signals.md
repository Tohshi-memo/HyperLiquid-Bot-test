# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T06:37:30.995734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `13`; crypto_alt avg `0.2095` n `237`; crypto_major avg `0.2203` n `8`; equity avg `0.0571` n `151`; fx avg `-0.0007` n `6`; index avg `0.0129` n `26`; metal avg `0.0256` n `20`; unknown avg `-0.0027` n `1198`
- 1h: commodity avg `-0.0058` n `13`; crypto_alt avg `0.2433` n `237`; crypto_major avg `0.0159` n `8`; equity avg `0.036` n `151`; fx avg `-0.0078` n `6`; index avg `0.0076` n `26`; metal avg `-0.114` n `20`; unknown avg `-0.2176` n `1178`
- 4h: commodity avg `-0.0374` n `13`; crypto_alt avg `-0.002` n `237`; crypto_major avg `-0.0779` n `8`; equity avg `-0.2072` n `151`; fx avg `-0.0586` n `6`; index avg `-0.0698` n `26`; metal avg `-0.1075` n `20`; unknown avg `0.5093` n `1172`
- 24h: commodity avg `-0.0165` n `13`; crypto_alt avg `2.7701` n `237`; crypto_major avg `1.8847` n `8`; equity avg `2.5874` n `151`; fx avg `-0.0076` n `6`; index avg `0.32` n `26`; metal avg `-0.1813` n `20`; unknown avg `5271.5213` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
