# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T13:13:44.662156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0689` n `12`; crypto_alt avg `0.0655` n `228`; crypto_major avg `-0.0108` n `8`; equity avg `-0.1646` n `86`; fx avg `0.0083` n `6`; index avg `-0.0222` n `23`; metal avg `0.2068` n `20`; unknown avg `0.1283` n `765`
- 1h: commodity avg `0.1264` n `12`; crypto_alt avg `0.1607` n `228`; crypto_major avg `0.3078` n `8`; equity avg `0.1078` n `86`; fx avg `0.0363` n `6`; index avg `0.0328` n `23`; metal avg `0.5639` n `20`; unknown avg `0.1088` n `765`
- 4h: commodity avg `0.1611` n `12`; crypto_alt avg `-0.6652` n `228`; crypto_major avg `-0.7491` n `8`; equity avg `0.0551` n `86`; fx avg `-0.0096` n `6`; index avg `0.0407` n `23`; metal avg `0.5562` n `20`; unknown avg `-0.0625` n `765`
- 24h: commodity avg `0.2119` n `12`; crypto_alt avg `-1.1526` n `228`; crypto_major avg `-0.8352` n `8`; equity avg `0.582` n `86`; fx avg `0.0406` n `6`; index avg `0.5617` n `23`; metal avg `0.3928` n `20`; unknown avg `-0.4249` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
