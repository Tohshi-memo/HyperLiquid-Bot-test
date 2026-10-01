# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T17:37:37.727443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `13`; crypto_alt avg `0.2053` n `234`; crypto_major avg `0.1427` n `8`; equity avg `0.3703` n `142`; fx avg `-0.0144` n `6`; index avg `0.0678` n `26`; metal avg `0.039` n `20`; unknown avg `1.55` n `975`
- 1h: commodity avg `0.0906` n `13`; crypto_alt avg `0.7068` n `234`; crypto_major avg `0.7375` n `8`; equity avg `0.8857` n `142`; fx avg `-0.0573` n `6`; index avg `0.153` n `26`; metal avg `0.1304` n `20`; unknown avg `0.994` n `973`
- 4h: commodity avg `-0.0058` n `13`; crypto_alt avg `0.3568` n `234`; crypto_major avg `0.3198` n `8`; equity avg `0.8213` n `142`; fx avg `-0.1751` n `6`; index avg `0.0478` n `26`; metal avg `0.067` n `20`; unknown avg `1.1806` n `909`
- 24h: commodity avg `-0.2036` n `13`; crypto_alt avg `-0.4266` n `234`; crypto_major avg `0.2502` n `8`; equity avg `1.2185` n `142`; fx avg `-0.1503` n `6`; index avg `0.1596` n `26`; metal avg `0.062` n `20`; unknown avg `-0.0568` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
