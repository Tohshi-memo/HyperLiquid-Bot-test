# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T05:37:32.222042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `0.0221` n `228`; crypto_major avg `-0.0447` n `8`; equity avg `-0.0195` n `74`; fx avg `-0.0113` n `6`; index avg `-0.0119` n `23`; metal avg `-0.1815` n `18`; unknown avg `1.0318` n `645`
- 1h: commodity avg `-0.0339` n `12`; crypto_alt avg `-0.4272` n `228`; crypto_major avg `-0.2531` n `8`; equity avg `-0.0464` n `74`; fx avg `-0.0056` n `6`; index avg `-0.0564` n `23`; metal avg `-0.1823` n `18`; unknown avg `0.2067` n `645`
- 4h: commodity avg `-0.081` n `12`; crypto_alt avg `-0.628` n `228`; crypto_major avg `-0.516` n `8`; equity avg `-0.0077` n `74`; fx avg `0.0092` n `6`; index avg `-0.0739` n `23`; metal avg `-0.1922` n `18`; unknown avg `-1.2472` n `629`
- 24h: commodity avg `-0.7702` n `12`; crypto_alt avg `1.2937` n `228`; crypto_major avg `1.5907` n `8`; equity avg `0.7105` n `74`; fx avg `-0.0385` n `6`; index avg `0.1811` n `23`; metal avg `0.1455` n `18`; unknown avg `-1.058` n `603`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
