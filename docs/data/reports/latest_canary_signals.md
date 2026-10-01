# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T04:52:26.828943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `0.185` n `234`; crypto_major avg `0.4989` n `8`; equity avg `0.1112` n `142`; fx avg `-0.0115` n `6`; index avg `0.0001` n `26`; metal avg `0.0325` n `20`; unknown avg `0.0952` n `974`
- 1h: commodity avg `0.0502` n `13`; crypto_alt avg `0.0314` n `234`; crypto_major avg `0.4313` n `8`; equity avg `0.2432` n `142`; fx avg `-0.0184` n `6`; index avg `0.0425` n `26`; metal avg `0.0598` n `20`; unknown avg `0.2785` n `966`
- 4h: commodity avg `-0.7627` n `13`; crypto_alt avg `0.9238` n `234`; crypto_major avg `0.6543` n `8`; equity avg `0.8824` n `142`; fx avg `-0.0419` n `6`; index avg `0.1967` n `26`; metal avg `0.3011` n `20`; unknown avg `0.6795` n `966`
- 24h: commodity avg `-0.5994` n `13`; crypto_alt avg `1.4416` n `234`; crypto_major avg `1.5179` n `8`; equity avg `0.6637` n `142`; fx avg `0.1531` n `6`; index avg `0.1993` n `26`; metal avg `0.0213` n `20`; unknown avg `778.1993` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
