# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T22:52:28.359782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `0.1126` n `239`; crypto_major avg `0.2798` n `8`; equity avg `0.3516` n `166`; fx avg `0.0106` n `6`; index avg `0.0319` n `27`; metal avg `0.0116` n `20`; unknown avg `164.1581` n `1256`
- 1h: commodity avg `-0.0084` n `13`; crypto_alt avg `-0.384` n `239`; crypto_major avg `-0.162` n `8`; equity avg `0.0063` n `166`; fx avg `0.0394` n `6`; index avg `-0.0388` n `27`; metal avg `-0.0323` n `20`; unknown avg `0.5218` n `1234`
- 4h: commodity avg `-0.0638` n `13`; crypto_alt avg `-0.2504` n `239`; crypto_major avg `-0.0794` n `8`; equity avg `0.1117` n `166`; fx avg `0.0941` n `6`; index avg `-0.0409` n `27`; metal avg `-0.0595` n `20`; unknown avg `-0.4627` n `1202`
- 24h: commodity avg `-0.1602` n `13`; crypto_alt avg `0.4872` n `239`; crypto_major avg `0.9059` n `8`; equity avg `0.9888` n `166`; fx avg `0.0718` n `6`; index avg `0.0916` n `27`; metal avg `0.0053` n `20`; unknown avg `242.8165` n `1042`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
