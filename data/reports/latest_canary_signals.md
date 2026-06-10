# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T03:22:31.923020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0715` n `12`; crypto_alt avg `0.0152` n `228`; crypto_major avg `0.1433` n `8`; equity avg `0.0725` n `74`; fx avg `0.0081` n `6`; index avg `-0.003` n `23`; metal avg `0.0137` n `18`; unknown avg `-0.1175` n `547`
- 1h: commodity avg `0.1475` n `12`; crypto_alt avg `-0.2` n `228`; crypto_major avg `-0.1459` n `8`; equity avg `-0.0597` n `74`; fx avg `0.0279` n `6`; index avg `-0.1232` n `23`; metal avg `-0.3674` n `18`; unknown avg `-0.154` n `547`
- 4h: commodity avg `-0.0545` n `12`; crypto_alt avg `-0.5531` n `228`; crypto_major avg `-0.9205` n `8`; equity avg `-0.1972` n `74`; fx avg `-0.0014` n `6`; index avg `-0.1682` n `23`; metal avg `-1.2426` n `18`; unknown avg `-0.3882` n `547`
- 24h: commodity avg `-0.411` n `12`; crypto_alt avg `-0.0011` n `228`; crypto_major avg `-2.8167` n `8`; equity avg `-2.6135` n `74`; fx avg `0.137` n `6`; index avg `-1.1486` n `23`; metal avg `-2.8653` n `18`; unknown avg `-0.3114` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.038`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0364`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0349`, n `668`, weak_sample_signal
