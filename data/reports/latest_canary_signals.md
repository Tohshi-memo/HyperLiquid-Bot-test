# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T10:22:34.223375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.1325` n `228`; crypto_major avg `-0.0885` n `8`; equity avg `0.0065` n `74`; fx avg `0.0029` n `6`; index avg `-0.0557` n `23`; metal avg `0.0005` n `18`; unknown avg `13.4128` n `644`
- 1h: commodity avg `-0.9247` n `12`; crypto_alt avg `-0.0957` n `228`; crypto_major avg `-0.2186` n `8`; equity avg `-0.1452` n `74`; fx avg `0.0258` n `6`; index avg `-0.1212` n `23`; metal avg `-0.197` n `18`; unknown avg `0.158` n `635`
- 4h: commodity avg `-0.1342` n `12`; crypto_alt avg `1.2888` n `228`; crypto_major avg `0.5495` n `8`; equity avg `0.2019` n `74`; fx avg `0.0024` n `6`; index avg `-0.0736` n `23`; metal avg `0.0607` n `18`; unknown avg `0.472` n `635`
- 24h: commodity avg `0.1432` n `12`; crypto_alt avg `0.5638` n `228`; crypto_major avg `-0.0563` n `8`; equity avg `-0.7376` n `74`; fx avg `0.011` n `6`; index avg `0.5526` n `23`; metal avg `0.2449` n `18`; unknown avg `30.7954` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
