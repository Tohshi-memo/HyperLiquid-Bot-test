# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T01:37:25.617723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `-0.3311` n `228`; crypto_major avg `-0.3785` n `8`; equity avg `-0.3341` n `86`; fx avg `0.0085` n `6`; index avg `-0.075` n `23`; metal avg `-0.1326` n `20`; unknown avg `2.9123` n `716`
- 1h: commodity avg `0.0301` n `12`; crypto_alt avg `0.1507` n `228`; crypto_major avg `-0.0461` n `8`; equity avg `-0.2638` n `86`; fx avg `-0.0298` n `6`; index avg `-0.0432` n `23`; metal avg `-0.2128` n `20`; unknown avg `1.6744` n `716`
- 4h: commodity avg `0.0064` n `12`; crypto_alt avg `-0.512` n `228`; crypto_major avg `-0.5086` n `8`; equity avg `-1.2073` n `86`; fx avg `0.0317` n `6`; index avg `-0.2817` n `23`; metal avg `-0.3655` n `20`; unknown avg `0.2695` n `716`
- 24h: commodity avg `-0.5062` n `12`; crypto_alt avg `-1.5609` n `228`; crypto_major avg `-1.3201` n `8`; equity avg `-1.4897` n `85`; fx avg `-0.011` n `6`; index avg `-0.2486` n `23`; metal avg `-0.5832` n `18`; unknown avg `0.0455` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
