# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T06:07:30.192333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1003` n `12`; crypto_alt avg `-0.0088` n `228`; crypto_major avg `0.0339` n `8`; equity avg `0.0008` n `74`; fx avg `0.0052` n `6`; index avg `0.034` n `23`; metal avg `0.0852` n `18`; unknown avg `-0.1734` n `535`
- 1h: commodity avg `-0.1092` n `12`; crypto_alt avg `-0.4254` n `228`; crypto_major avg `-0.3564` n `8`; equity avg `-0.5554` n `74`; fx avg `-0.0241` n `6`; index avg `-0.3312` n `23`; metal avg `-0.1835` n `18`; unknown avg `-0.4141` n `535`
- 4h: commodity avg `-0.1716` n `12`; crypto_alt avg `-0.3763` n `228`; crypto_major avg `-0.0761` n `8`; equity avg `-0.4811` n `74`; fx avg `0.0002` n `6`; index avg `-0.3375` n `23`; metal avg `-0.285` n `18`; unknown avg `1.1174` n `535`
- 24h: commodity avg `-2.2362` n `12`; crypto_alt avg `1.6693` n `228`; crypto_major avg `2.0406` n `8`; equity avg `3.2352` n `74`; fx avg `-0.0159` n `6`; index avg `1.7128` n `23`; metal avg `2.9313` n `18`; unknown avg `1.7014` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
