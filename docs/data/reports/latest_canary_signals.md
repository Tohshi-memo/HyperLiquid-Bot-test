# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T09:52:26.377419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `13`; crypto_alt avg `-0.0381` n `239`; crypto_major avg `-0.075` n `8`; equity avg `-0.0779` n `163`; fx avg `0.0132` n `6`; index avg `-0.016` n `27`; metal avg `0.0149` n `20`; unknown avg `0.7411` n `1266`
- 1h: commodity avg `0.0927` n `13`; crypto_alt avg `0.0576` n `239`; crypto_major avg `-0.0334` n `8`; equity avg `0.2582` n `163`; fx avg `0.0432` n `6`; index avg `0.0313` n `27`; metal avg `0.111` n `20`; unknown avg `151.5513` n `1252`
- 4h: commodity avg `-0.1257` n `13`; crypto_alt avg `0.3351` n `239`; crypto_major avg `0.0615` n `8`; equity avg `0.5321` n `163`; fx avg `-0.066` n `6`; index avg `0.0853` n `27`; metal avg `-0.2849` n `20`; unknown avg `162.6522` n `1168`
- 24h: commodity avg `-0.2362` n `13`; crypto_alt avg `1.1381` n `239`; crypto_major avg `1.2793` n `8`; equity avg `1.9695` n `163`; fx avg `-0.12` n `6`; index avg `0.1818` n `27`; metal avg `-0.9416` n `20`; unknown avg `5.7981` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
