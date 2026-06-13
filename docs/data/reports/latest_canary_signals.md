# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T23:52:29.118461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2752` n `12`; crypto_alt avg `-0.2254` n `228`; crypto_major avg `-0.1138` n `8`; equity avg `0.003` n `74`; fx avg `-0.0028` n `6`; index avg `0.002` n `23`; metal avg `-0.0123` n `18`; unknown avg `-0.1838` n `645`
- 1h: commodity avg `-0.3233` n `12`; crypto_alt avg `-0.2855` n `228`; crypto_major avg `-0.0378` n `8`; equity avg `-0.016` n `74`; fx avg `-0.0131` n `6`; index avg `-0.0456` n `23`; metal avg `-0.0194` n `18`; unknown avg `0.8197` n `645`
- 4h: commodity avg `-0.2142` n `12`; crypto_alt avg `-0.2737` n `228`; crypto_major avg `0.2799` n `8`; equity avg `0.074` n `74`; fx avg `-0.0232` n `6`; index avg `0.0698` n `23`; metal avg `0.2058` n `18`; unknown avg `8.2666` n `644`
- 24h: commodity avg `-0.6653` n `12`; crypto_alt avg `2.2964` n `228`; crypto_major avg `1.5168` n `8`; equity avg `0.3717` n `74`; fx avg `0.0055` n `6`; index avg `0.4595` n `23`; metal avg `0.2741` n `18`; unknown avg `1.0642` n `611`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
