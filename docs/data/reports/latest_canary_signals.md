# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T16:52:29.581066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `0.03` n `228`; crypto_major avg `-0.0035` n `8`; equity avg `-0.1416` n `74`; fx avg `-0.0067` n `6`; index avg `-0.1005` n `23`; metal avg `-0.1778` n `18`; unknown avg `0.0947` n `644`
- 1h: commodity avg `0.1479` n `12`; crypto_alt avg `-0.5251` n `228`; crypto_major avg `-0.5599` n `8`; equity avg `-0.2678` n `74`; fx avg `-0.0081` n `6`; index avg `-0.0732` n `23`; metal avg `-0.1255` n `18`; unknown avg `0.1427` n `644`
- 4h: commodity avg `0.2131` n `12`; crypto_alt avg `-0.0846` n `228`; crypto_major avg `-0.1435` n `8`; equity avg `-0.0219` n `74`; fx avg `-0.0199` n `6`; index avg `0.0258` n `23`; metal avg `-0.1002` n `18`; unknown avg `-2.2708` n `644`
- 24h: commodity avg `-0.5828` n `12`; crypto_alt avg `1.2779` n `228`; crypto_major avg `-0.234` n `8`; equity avg `-0.2155` n `74`; fx avg `0.0163` n `6`; index avg `0.4848` n `23`; metal avg `0.3935` n `18`; unknown avg `-2.0027` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
