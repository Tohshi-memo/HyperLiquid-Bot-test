# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T02:22:39.664954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0858` n `13`; crypto_alt avg `-0.1239` n `239`; crypto_major avg `-0.09` n `8`; equity avg `-0.3381` n `162`; fx avg `0.0213` n `6`; index avg `-0.0367` n `27`; metal avg `-0.0226` n `20`; unknown avg `0.2248` n `1260`
- 1h: commodity avg `-0.0345` n `13`; crypto_alt avg `-0.209` n `239`; crypto_major avg `-0.3155` n `8`; equity avg `-0.4188` n `162`; fx avg `0.0335` n `6`; index avg `-0.0495` n `27`; metal avg `0.0012` n `20`; unknown avg `-0.08` n `1260`
- 4h: commodity avg `-0.0849` n `13`; crypto_alt avg `-0.014` n `239`; crypto_major avg `-0.2272` n `8`; equity avg `0.6178` n `162`; fx avg `0.004` n `6`; index avg `0.1144` n `27`; metal avg `0.2827` n `20`; unknown avg `0.8023` n `1221`
- 24h: commodity avg `0.7625` n `13`; crypto_alt avg `-1.125` n `239`; crypto_major avg `-2.302` n `8`; equity avg `-1.0083` n `162`; fx avg `-0.0677` n `6`; index avg `0.0483` n `27`; metal avg `-0.4776` n `20`; unknown avg `51.2421` n `1119`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
