# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T09:07:31.074090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.079` n `13`; crypto_alt avg `0.002` n `239`; crypto_major avg `0.0468` n `8`; equity avg `0.2495` n `163`; fx avg `-0.0081` n `6`; index avg `0.0193` n `27`; metal avg `0.035` n `20`; unknown avg `47.8657` n `1252`
- 1h: commodity avg `-0.0274` n `13`; crypto_alt avg `-0.0007` n `239`; crypto_major avg `-0.0982` n `8`; equity avg `0.193` n `163`; fx avg `-0.0489` n `6`; index avg `0.0305` n `27`; metal avg `-0.063` n `20`; unknown avg `50.7883` n `1204`
- 4h: commodity avg `-0.0319` n `13`; crypto_alt avg `1.0293` n `239`; crypto_major avg `0.6782` n `8`; equity avg `1.1727` n `163`; fx avg `-0.0971` n `6`; index avg `0.1375` n `27`; metal avg `-0.2642` n `20`; unknown avg `43.4176` n `1166`
- 24h: commodity avg `-0.1709` n `13`; crypto_alt avg `0.9283` n `239`; crypto_major avg `1.321` n `8`; equity avg `1.7822` n `163`; fx avg `-0.1469` n `6`; index avg `0.1667` n `27`; metal avg `-1.0304` n `20`; unknown avg `5.9762` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
