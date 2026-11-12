# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T00:52:26.729182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0286` n `13`; crypto_alt avg `-0.0098` n `239`; crypto_major avg `0.112` n `8`; equity avg `-0.192` n `161`; fx avg `0.0024` n `6`; index avg `-0.0099` n `27`; metal avg `0.026` n `20`; unknown avg `1.1098` n `1262`
- 1h: commodity avg `-0.02` n `13`; crypto_alt avg `0.2993` n `239`; crypto_major avg `0.3173` n `8`; equity avg `-0.065` n `161`; fx avg `-0.0225` n `6`; index avg `0.0123` n `27`; metal avg `0.0756` n `20`; unknown avg `1.5986` n `1250`
- 4h: commodity avg `-0.0281` n `13`; crypto_alt avg `-1.2062` n `239`; crypto_major avg `-1.0246` n `8`; equity avg `-1.4027` n `161`; fx avg `-0.0529` n `6`; index avg `-0.124` n `27`; metal avg `-0.0484` n `20`; unknown avg `1.7795` n `1204`
- 24h: commodity avg `0.1595` n `13`; crypto_alt avg `-1.0293` n `239`; crypto_major avg `0.3263` n `8`; equity avg `2.032` n `161`; fx avg `-0.1463` n `6`; index avg `0.2074` n `27`; metal avg `-0.1026` n `20`; unknown avg `2.7297` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
