# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T14:07:26.497389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1022` n `12`; crypto_alt avg `-0.116` n `228`; crypto_major avg `-0.2611` n `8`; equity avg `0.0346` n `72`; fx avg `0.0036` n `6`; index avg `0.2429` n `23`; metal avg `0.0915` n `18`; unknown avg `-0.2611` n `420`
- 1h: commodity avg `-0.283` n `12`; crypto_alt avg `0.199` n `228`; crypto_major avg `-0.509` n `8`; equity avg `-1.4072` n `72`; fx avg `-0.0041` n `6`; index avg `-0.4236` n `23`; metal avg `-0.588` n `18`; unknown avg `0.0871` n `420`
- 4h: commodity avg `-0.8875` n `12`; crypto_alt avg `0.3361` n `228`; crypto_major avg `-0.8746` n `8`; equity avg `-1.6276` n `72`; fx avg `-0.046` n `6`; index avg `-0.5618` n `23`; metal avg `-0.8198` n `18`; unknown avg `-0.3021` n `420`
- 24h: commodity avg `0.714` n `12`; crypto_alt avg `-0.6986` n `228`; crypto_major avg `-3.5506` n `8`; equity avg `-1.0286` n `72`; fx avg `0.0277` n `6`; index avg `0.0604` n `23`; metal avg `-1.6279` n `18`; unknown avg `-0.2119` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
