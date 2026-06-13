# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T17:37:29.227690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1057` n `12`; crypto_alt avg `0.107` n `228`; crypto_major avg `0.0867` n `8`; equity avg `-0.0047` n `74`; fx avg `0.0146` n `6`; index avg `-0.0884` n `23`; metal avg `-0.1048` n `18`; unknown avg `0.0249` n `644`
- 1h: commodity avg `-0.165` n `12`; crypto_alt avg `0.4416` n `228`; crypto_major avg `0.1007` n `8`; equity avg `-0.0993` n `74`; fx avg `0.0239` n `6`; index avg `-0.1289` n `23`; metal avg `-0.1679` n `18`; unknown avg `0.1198` n `644`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.4031` n `228`; crypto_major avg `-0.1102` n `8`; equity avg `-0.0558` n `74`; fx avg `0.0118` n `6`; index avg `-0.0927` n `23`; metal avg `-0.0369` n `18`; unknown avg `-2.0218` n `644`
- 24h: commodity avg `-0.7339` n `12`; crypto_alt avg `1.794` n `228`; crypto_major avg `-0.2463` n `8`; equity avg `-0.2179` n `74`; fx avg `0.0385` n `6`; index avg `0.4073` n `23`; metal avg `0.3747` n `18`; unknown avg `-1.939` n `611`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
