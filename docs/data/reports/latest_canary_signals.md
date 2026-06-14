# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T00:37:25.457333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.0162` n `228`; crypto_major avg `0.1576` n `8`; equity avg `0.0696` n `74`; fx avg `0.0002` n `6`; index avg `-0.0278` n `23`; metal avg `-0.1603` n `18`; unknown avg `7.3497` n `645`
- 1h: commodity avg `-0.2705` n `12`; crypto_alt avg `-0.1619` n `228`; crypto_major avg `0.006` n `8`; equity avg `0.0449` n `74`; fx avg `-0.0003` n `6`; index avg `-0.0336` n `23`; metal avg `-0.1732` n `18`; unknown avg `-0.5011` n `645`
- 4h: commodity avg `-0.2327` n `12`; crypto_alt avg `0.134` n `228`; crypto_major avg `0.5064` n `8`; equity avg `0.1113` n `74`; fx avg `-0.0116` n `6`; index avg `-0.071` n `23`; metal avg `-0.0704` n `18`; unknown avg `5.3966` n `644`
- 24h: commodity avg `-0.7254` n `12`; crypto_alt avg `2.0035` n `228`; crypto_major avg `1.6162` n `8`; equity avg `0.3195` n `74`; fx avg `-0.0139` n `6`; index avg `0.3138` n `23`; metal avg `0.0996` n `18`; unknown avg `0.8091` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
