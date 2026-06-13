# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T22:07:32.102546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0498` n `12`; crypto_alt avg `-0.0404` n `228`; crypto_major avg `-0.1406` n `8`; equity avg `-0.0394` n `74`; fx avg `0.0386` n `6`; index avg `-0.0592` n `23`; metal avg `-0.8613` n `18`; unknown avg `6.5132` n `644`
- 1h: commodity avg `0.0559` n `12`; crypto_alt avg `0.4576` n `228`; crypto_major avg `0.4478` n `8`; equity avg `0.0554` n `74`; fx avg `-0.0371` n `6`; index avg `0.0465` n `23`; metal avg `0.0696` n `18`; unknown avg `1.888` n `644`
- 4h: commodity avg `0.2175` n `12`; crypto_alt avg `0.3198` n `228`; crypto_major avg `0.6685` n `8`; equity avg `0.2466` n `74`; fx avg `0.0024` n `6`; index avg `0.1954` n `23`; metal avg `-0.2011` n `18`; unknown avg `1.1972` n `644`
- 24h: commodity avg `-0.5771` n `12`; crypto_alt avg `2.6302` n `228`; crypto_major avg `1.3524` n `8`; equity avg `0.4814` n `74`; fx avg `0.0693` n `6`; index avg `0.5146` n `23`; metal avg `0.1264` n `18`; unknown avg `-0.3238` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
