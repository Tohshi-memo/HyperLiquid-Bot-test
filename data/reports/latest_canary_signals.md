# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T09:22:28.462067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0069` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0433` n `12`; crypto_alt avg `-0.2371` n `232`; crypto_major avg `-0.2554` n `8`; equity avg `-0.1286` n `132`; fx avg `-0.0119` n `6`; index avg `-0.0352` n `26`; metal avg `-0.0494` n `20`; unknown avg `0.0818` n `792`
- 1h: commodity avg `0.0266` n `12`; crypto_alt avg `-0.5725` n `232`; crypto_major avg `-0.6371` n `8`; equity avg `-0.3594` n `132`; fx avg `0.0026` n `6`; index avg `-0.0899` n `26`; metal avg `-0.085` n `20`; unknown avg `0.5328` n `790`
- 4h: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.8114` n `232`; crypto_major avg `-1.1151` n `8`; equity avg `-0.5474` n `132`; fx avg `-0.0686` n `6`; index avg `-0.1082` n `26`; metal avg `-0.0093` n `20`; unknown avg `0.359` n `770`
- 24h: commodity avg `0.5787` n `12`; crypto_alt avg `-0.1145` n `232`; crypto_major avg `-1.7361` n `8`; equity avg `-1.606` n `130`; fx avg `-0.2074` n `6`; index avg `-0.2731` n `26`; metal avg `-0.454` n `20`; unknown avg `0.033` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
