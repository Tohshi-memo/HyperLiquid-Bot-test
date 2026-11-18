# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T09:37:26.738288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0878` n `13`; crypto_alt avg `0.1236` n `239`; crypto_major avg `0.1378` n `8`; equity avg `0.1725` n `163`; fx avg `0.0261` n `6`; index avg `0.0227` n `27`; metal avg `0.1202` n `20`; unknown avg `0.7612` n `1266`
- 1h: commodity avg `0.0326` n `13`; crypto_alt avg `0.2573` n `239`; crypto_major avg `0.0339` n `8`; equity avg `0.3676` n `163`; fx avg `0.0146` n `6`; index avg `0.0611` n `27`; metal avg `0.0909` n `20`; unknown avg `75.7498` n `1224`
- 4h: commodity avg `-0.0972` n `13`; crypto_alt avg `0.4782` n `239`; crypto_major avg `0.0552` n `8`; equity avg `0.7372` n `163`; fx avg `-0.0685` n `6`; index avg `0.123` n `27`; metal avg `-0.3023` n `20`; unknown avg `66.9925` n `1166`
- 24h: commodity avg `-0.2146` n `13`; crypto_alt avg `1.2681` n `239`; crypto_major avg `1.4086` n `8`; equity avg `2.3741` n `163`; fx avg `-0.1109` n `6`; index avg `0.2364` n `27`; metal avg `-0.9256` n `20`; unknown avg `187.6952` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
