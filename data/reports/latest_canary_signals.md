# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T13:52:29.389553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1063` n `13`; crypto_alt avg `0.2046` n `237`; crypto_major avg `0.0839` n `8`; equity avg `-0.1425` n `151`; fx avg `0.022` n `6`; index avg `-0.0052` n `26`; metal avg `0.0275` n `20`; unknown avg `-0.1311` n `1166`
- 1h: commodity avg `-0.1871` n `13`; crypto_alt avg `0.3965` n `237`; crypto_major avg `0.1942` n `8`; equity avg `-0.0088` n `151`; fx avg `0.0359` n `6`; index avg `0.0381` n `26`; metal avg `0.0845` n `20`; unknown avg `6.1634` n `1162`
- 4h: commodity avg `-0.3931` n `13`; crypto_alt avg `1.0371` n `237`; crypto_major avg `0.7398` n `8`; equity avg `-0.0231` n `151`; fx avg `0.0511` n `6`; index avg `0.0687` n `26`; metal avg `0.0865` n `20`; unknown avg `4.3946` n `1156`
- 24h: commodity avg `0.0142` n `13`; crypto_alt avg `0.909` n `237`; crypto_major avg `0.1125` n `8`; equity avg `-1.9853` n `151`; fx avg `0.0246` n `6`; index avg `-0.2095` n `26`; metal avg `-0.0832` n `20`; unknown avg `3.9576` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
