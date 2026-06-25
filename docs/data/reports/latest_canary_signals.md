# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T09:37:35.164362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `0.1869` n `228`; crypto_major avg `0.0933` n `8`; equity avg `0.0618` n `86`; fx avg `0.0056` n `6`; index avg `0.0212` n `23`; metal avg `-0.0091` n `20`; unknown avg `0.0721` n `765`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `-0.2979` n `228`; crypto_major avg `-0.094` n `8`; equity avg `-0.0666` n `86`; fx avg `0.0223` n `6`; index avg `-0.0185` n `23`; metal avg `-0.0082` n `20`; unknown avg `-0.0375` n `765`
- 4h: commodity avg `0.1298` n `12`; crypto_alt avg `-0.4313` n `228`; crypto_major avg `-0.1201` n `8`; equity avg `0.0309` n `86`; fx avg `0.0359` n `6`; index avg `-0.0419` n `23`; metal avg `0.1781` n `20`; unknown avg `0.067` n `733`
- 24h: commodity avg `-0.2591` n `12`; crypto_alt avg `-1.1996` n `228`; crypto_major avg `-0.7445` n `8`; equity avg `0.082` n `86`; fx avg `-0.0178` n `6`; index avg `0.5123` n `23`; metal avg `-1.2881` n `20`; unknown avg `-0.6096` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
