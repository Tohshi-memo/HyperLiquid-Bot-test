# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T03:37:28.749075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3644` n `13`; crypto_alt avg `0.2997` n `234`; crypto_major avg `0.1638` n `8`; equity avg `0.0016` n `142`; fx avg `0.0078` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0108` n `20`; unknown avg `0.6756` n `974`
- 1h: commodity avg `-0.4278` n `13`; crypto_alt avg `0.6476` n `234`; crypto_major avg `0.135` n `8`; equity avg `0.1493` n `142`; fx avg `-0.0042` n `6`; index avg `0.015` n `26`; metal avg `0.0416` n `20`; unknown avg `0.0905` n `972`
- 4h: commodity avg `-0.4585` n `13`; crypto_alt avg `0.5681` n `234`; crypto_major avg `-0.1695` n `8`; equity avg `0.4327` n `142`; fx avg `0.0856` n `6`; index avg `0.1016` n `26`; metal avg `0.0551` n `20`; unknown avg `0.4135` n `942`
- 24h: commodity avg `-0.3518` n `13`; crypto_alt avg `1.4967` n `234`; crypto_major avg `0.7784` n `8`; equity avg `0.3465` n `142`; fx avg `0.2238` n `6`; index avg `0.1339` n `26`; metal avg `-0.12` n `20`; unknown avg `777.2607` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
