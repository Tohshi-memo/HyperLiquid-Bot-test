# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T21:36:06.022166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `0.1051` n `228`; crypto_major avg `0.0793` n `8`; equity avg `0.011` n `74`; fx avg `0.0054` n `6`; index avg `0.098` n `23`; metal avg `0.8458` n `18`; unknown avg `0.6213` n `644`
- 1h: commodity avg `0.1771` n `12`; crypto_alt avg `0.0097` n `228`; crypto_major avg `0.1523` n `8`; equity avg `0.0241` n `74`; fx avg `0.0258` n `6`; index avg `0.1225` n `23`; metal avg `0.8929` n `18`; unknown avg `3.8661` n `644`
- 4h: commodity avg `0.2003` n `12`; crypto_alt avg `-0.3852` n `228`; crypto_major avg `0.2198` n `8`; equity avg `0.289` n `74`; fx avg `0.0174` n `6`; index avg `0.2384` n `23`; metal avg `0.8758` n `18`; unknown avg `1.0201` n `644`
- 24h: commodity avg `-0.5174` n `12`; crypto_alt avg `1.8075` n `228`; crypto_major avg `0.6679` n `8`; equity avg `0.4617` n `74`; fx avg `0.0901` n `6`; index avg `0.7352` n `23`; metal avg `1.0768` n `18`; unknown avg `-0.313` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
