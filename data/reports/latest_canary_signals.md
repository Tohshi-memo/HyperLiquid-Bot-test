# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T23:52:28.650264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `13`; crypto_alt avg `-0.2674` n `239`; crypto_major avg `-0.2428` n `8`; equity avg `-0.3507` n `166`; fx avg `0.0039` n `6`; index avg `-0.0346` n `27`; metal avg `-0.0151` n `20`; unknown avg `-0.0018` n `1262`
- 1h: commodity avg `-0.0182` n `13`; crypto_alt avg `-0.1139` n `239`; crypto_major avg `-0.1622` n `8`; equity avg `-0.0256` n `166`; fx avg `-0.0008` n `6`; index avg `0.01` n `27`; metal avg `0.0168` n `20`; unknown avg `0.1562` n `1246`
- 4h: commodity avg `0.1472` n `13`; crypto_alt avg `1.1203` n `239`; crypto_major avg `1.007` n `8`; equity avg `0.7632` n `166`; fx avg `-0.0335` n `6`; index avg `0.0633` n `27`; metal avg `0.1182` n `20`; unknown avg `2.4185` n `1198`
- 24h: commodity avg `0.2639` n `13`; crypto_alt avg `-4.8334` n `239`; crypto_major avg `-5.6969` n `8`; equity avg `-5.7529` n `166`; fx avg `-0.0295` n `6`; index avg `-0.6282` n `27`; metal avg `-0.6056` n `20`; unknown avg `12.2644` n `1121`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
