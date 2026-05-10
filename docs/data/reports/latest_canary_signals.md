# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T01:52:18.588514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.1441` n `228`; crypto_major avg `0.1804` n `8`; equity avg `-0.029` n `65`; fx avg `0.0` n `5`; index avg `-0.0079` n `23`; metal avg `-0.0026` n `18`; unknown avg `-0.0127` n `376`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.2948` n `228`; crypto_major avg `-0.056` n `8`; equity avg `-0.0473` n `65`; fx avg `0.0` n `5`; index avg `0.0251` n `23`; metal avg `0.0029` n `18`; unknown avg `-0.349` n `376`
- 4h: commodity avg `-0.0427` n `12`; crypto_alt avg `-0.9917` n `228`; crypto_major avg `-0.4693` n `8`; equity avg `0.1279` n `65`; fx avg `0.0002` n `5`; index avg `0.102` n `23`; metal avg `0.0206` n `18`; unknown avg `-0.6686` n `376`
- 24h: commodity avg `0.4942` n `12`; crypto_alt avg `-2.0938` n `228`; crypto_major avg `-0.989` n `8`; equity avg `0.6322` n `65`; fx avg `-0.0287` n `5`; index avg `0.3805` n `23`; metal avg `0.2` n `18`; unknown avg `-0.5374` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
