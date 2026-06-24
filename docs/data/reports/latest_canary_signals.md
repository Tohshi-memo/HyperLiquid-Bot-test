# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T08:22:26.908985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `0.058` n `228`; crypto_major avg `0.0493` n `8`; equity avg `-0.0034` n `86`; fx avg `0.004` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0424` n `20`; unknown avg `0.0036` n `764`
- 1h: commodity avg `-0.0857` n `12`; crypto_alt avg `-0.0269` n `228`; crypto_major avg `-0.171` n `8`; equity avg `0.1148` n `86`; fx avg `-0.0178` n `6`; index avg `0.017` n `23`; metal avg `-0.1589` n `20`; unknown avg `-0.0553` n `764`
- 4h: commodity avg `-0.1517` n `12`; crypto_alt avg `0.5277` n `228`; crypto_major avg `0.4166` n `8`; equity avg `0.8813` n `86`; fx avg `0.0402` n `6`; index avg `0.2567` n `23`; metal avg `0.17` n `20`; unknown avg `0.013` n `740`
- 24h: commodity avg `-0.5708` n `12`; crypto_alt avg `0.6394` n `228`; crypto_major avg `0.0721` n `8`; equity avg `5.3197` n `86`; fx avg `-0.026` n `6`; index avg `0.1456` n `23`; metal avg `-0.2826` n `20`; unknown avg `-0.1104` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
