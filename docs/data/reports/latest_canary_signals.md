# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T02:22:29.608608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `0.0721` n `228`; crypto_major avg `0.1083` n `8`; equity avg `-0.111` n `74`; fx avg `0.0091` n `6`; index avg `0.0024` n `23`; metal avg `0.017` n `18`; unknown avg `-0.1156` n `645`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `0.0749` n `228`; crypto_major avg `-0.084` n `8`; equity avg `0.0046` n `74`; fx avg `0.0125` n `6`; index avg `-0.0184` n `23`; metal avg `-0.0158` n `18`; unknown avg `93.173` n `645`
- 4h: commodity avg `-0.4991` n `12`; crypto_alt avg `-0.2332` n `228`; crypto_major avg `0.1653` n `8`; equity avg `0.0904` n `74`; fx avg `0.0126` n `6`; index avg `-0.0357` n `23`; metal avg `0.0019` n `18`; unknown avg `442.132` n `645`
- 24h: commodity avg `-0.6678` n `12`; crypto_alt avg `1.6362` n `228`; crypto_major avg `1.3969` n `8`; equity avg `0.3134` n `74`; fx avg `0.0187` n `6`; index avg `0.2246` n `23`; metal avg `0.2397` n `18`; unknown avg `0.1493` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
