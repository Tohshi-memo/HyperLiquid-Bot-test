# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T22:52:29.071373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0647` n `12`; crypto_alt avg `-0.0939` n `228`; crypto_major avg `-0.0085` n `8`; equity avg `0.0002` n `74`; fx avg `0.0166` n `6`; index avg `0.0055` n `23`; metal avg `-0.0018` n `18`; unknown avg `0.1229` n `645`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.1697` n `228`; crypto_major avg `-0.1772` n `8`; equity avg `-0.0138` n `74`; fx avg `0.0446` n `6`; index avg `-0.101` n `23`; metal avg `-0.6814` n `18`; unknown avg `0.9745` n `644`
- 4h: commodity avg `0.1815` n `12`; crypto_alt avg `0.4197` n `228`; crypto_major avg `0.5673` n `8`; equity avg `0.1997` n `74`; fx avg `-0.0278` n `6`; index avg `0.1035` n `23`; metal avg `0.0412` n `18`; unknown avg `1.686` n `644`
- 24h: commodity avg `-0.2329` n `12`; crypto_alt avg `2.6245` n `228`; crypto_major avg `1.4104` n `8`; equity avg `0.4279` n `74`; fx avg `0.0454` n `6`; index avg `0.5055` n `23`; metal avg `0.3119` n `18`; unknown avg `0.1827` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
