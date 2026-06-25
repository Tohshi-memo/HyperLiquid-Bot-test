# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T08:07:34.376360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.021` n `228`; crypto_major avg `-0.0969` n `8`; equity avg `0.0544` n `86`; fx avg `0.0091` n `6`; index avg `-0.0007` n `23`; metal avg `0.0922` n `20`; unknown avg `-0.0055` n `765`
- 1h: commodity avg `0.131` n `12`; crypto_alt avg `0.122` n `228`; crypto_major avg `-0.0452` n `8`; equity avg `0.0886` n `86`; fx avg `-0.0061` n `6`; index avg `0.0041` n `23`; metal avg `0.2819` n `20`; unknown avg `-0.0359` n `757`
- 4h: commodity avg `0.2256` n `12`; crypto_alt avg `1.1827` n `228`; crypto_major avg `1.3997` n `8`; equity avg `0.5248` n `86`; fx avg `-0.081` n `6`; index avg `0.0477` n `23`; metal avg `0.0133` n `20`; unknown avg `0.1755` n `733`
- 24h: commodity avg `-0.168` n `12`; crypto_alt avg `-0.8627` n `228`; crypto_major avg `-0.4916` n `8`; equity avg `0.0664` n `86`; fx avg `-0.031` n `6`; index avg `0.506` n `23`; metal avg `-1.47` n `20`; unknown avg `-0.6819` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
