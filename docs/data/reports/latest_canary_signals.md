# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T09:37:24.803370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `0.0739` n `228`; crypto_major avg `-0.0366` n `8`; equity avg `-0.0026` n `72`; fx avg `0.0187` n `6`; index avg `-0.022` n `23`; metal avg `-0.15` n `18`; unknown avg `-0.0885` n `420`
- 1h: commodity avg `0.1483` n `12`; crypto_alt avg `-0.3831` n `228`; crypto_major avg `-0.1525` n `8`; equity avg `-0.1242` n `72`; fx avg `0.01` n `6`; index avg `-0.0069` n `23`; metal avg `-0.1107` n `18`; unknown avg `-0.5341` n `420`
- 4h: commodity avg `0.846` n `12`; crypto_alt avg `0.5804` n `228`; crypto_major avg `0.2108` n `8`; equity avg `-0.1979` n `72`; fx avg `0.0239` n `6`; index avg `0.0117` n `23`; metal avg `-0.4466` n `18`; unknown avg `-0.1671` n `410`
- 24h: commodity avg `1.855` n `12`; crypto_alt avg `-0.9623` n `228`; crypto_major avg `-3.1882` n `8`; equity avg `0.5009` n `72`; fx avg `0.0575` n `6`; index avg `0.898` n `23`; metal avg `-1.5874` n `18`; unknown avg `0.5847` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
