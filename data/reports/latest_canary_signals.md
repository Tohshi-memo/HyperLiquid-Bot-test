# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T00:22:09.411855+00:00`
- Correlation status: `ready`
- Asset price records: `597`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2074` n `12`; crypto_alt avg `-0.0069` n `228`; crypto_major avg `0.0057` n `8`; equity avg `0.0604` n `65`; fx avg `0.0416` n `5`; index avg `-0.011` n `23`; metal avg `-0.2377` n `18`; unknown avg `-0.0407` n `365`
- 1h: commodity avg `0.115` n `12`; crypto_alt avg `0.3345` n `228`; crypto_major avg `0.2151` n `8`; equity avg `0.2432` n `65`; fx avg `0.0879` n `5`; index avg `0.1468` n `23`; metal avg `0.0462` n `18`; unknown avg `-0.1334` n `365`
- 4h: commodity avg `0.5694` n `12`; crypto_alt avg `0.1201` n `228`; crypto_major avg `-0.0872` n `8`; equity avg `-0.0906` n `65`; fx avg `0.0505` n `5`; index avg `0.1078` n `23`; metal avg `-0.4942` n `18`; unknown avg `-0.3192` n `365`
- 24h: commodity avg `0.7194` n `12`; crypto_alt avg `1.6338` n `228`; crypto_major avg `-1.5659` n `8`; equity avg `-0.9832` n `65`; fx avg `0.2101` n `5`; index avg `-0.6362` n `23`; metal avg `-0.1388` n `18`; unknown avg `-0.347` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1369`, n `593`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `593`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `593`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `593`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `589`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `589`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `589`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `589`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `589`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0722`, n `589`, weak_sample_signal
