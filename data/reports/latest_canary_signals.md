# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T22:04:19.148886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.4922` n `231`; crypto_major avg `-0.428` n `8`; equity avg `-0.117` n `122`; fx avg `-0.0026` n `6`; index avg `-0.0481` n `25`; metal avg `-0.0417` n `20`; unknown avg `0.1359` n `793`
- 1h: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.3198` n `231`; crypto_major avg `-0.0992` n `8`; equity avg `-0.1005` n `122`; fx avg `-0.0219` n `6`; index avg `-0.045` n `25`; metal avg `-0.0547` n `20`; unknown avg `0.1872` n `793`
- 4h: commodity avg `-0.0881` n `12`; crypto_alt avg `0.4708` n `231`; crypto_major avg `0.7085` n `8`; equity avg `0.0524` n `122`; fx avg `-0.1012` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0036` n `20`; unknown avg `1.856` n `793`
- 24h: commodity avg `-0.1755` n `12`; crypto_alt avg `4.0744` n `231`; crypto_major avg `1.7212` n `8`; equity avg `0.654` n `122`; fx avg `-0.1002` n `6`; index avg `0.0744` n `25`; metal avg `0.0689` n `20`; unknown avg `6.1748` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
