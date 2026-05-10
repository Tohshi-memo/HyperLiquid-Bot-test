# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T02:07:16.837614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.0516` n `228`; crypto_major avg `-0.0261` n `8`; equity avg `0.0025` n `65`; fx avg `0.0` n `5`; index avg `0.0334` n `23`; metal avg `0.0229` n `18`; unknown avg `0.0426` n `376`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0006` n `228`; crypto_major avg `0.0496` n `8`; equity avg `0.0334` n `65`; fx avg `0.0` n `5`; index avg `0.0371` n `23`; metal avg `0.0277` n `18`; unknown avg `-0.2265` n `376`
- 4h: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.9349` n `228`; crypto_major avg `-0.506` n `8`; equity avg `0.0495` n `65`; fx avg `0.0002` n `5`; index avg `0.1236` n `23`; metal avg `0.0307` n `18`; unknown avg `-0.6543` n `376`
- 24h: commodity avg `0.4731` n `12`; crypto_alt avg `-1.9169` n `228`; crypto_major avg `-1.0011` n `8`; equity avg `0.6343` n `65`; fx avg `-0.0287` n `5`; index avg `0.3295` n `23`; metal avg `0.1888` n `18`; unknown avg `-0.7124` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
