# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T09:37:30.476213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `0.0509` n `230`; crypto_major avg `-0.0169` n `8`; equity avg `-0.0277` n `114`; fx avg `0.0057` n `6`; index avg `0.0049` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.0269` n `795`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.0037` n `230`; crypto_major avg `-0.183` n `8`; equity avg `-0.4209` n `114`; fx avg `-0.0081` n `6`; index avg `-0.0596` n `25`; metal avg `-0.0375` n `20`; unknown avg `-0.0067` n `795`
- 4h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.6836` n `230`; crypto_major avg `0.2244` n `8`; equity avg `-0.9482` n `114`; fx avg `0.0029` n `6`; index avg `-0.134` n `25`; metal avg `-0.0342` n `20`; unknown avg `0.0172` n `761`
- 24h: commodity avg `0.5259` n `12`; crypto_alt avg `-0.5829` n `230`; crypto_major avg `0.1548` n `8`; equity avg `-2.6595` n `114`; fx avg `-0.0165` n `6`; index avg `-0.5307` n `25`; metal avg `-0.2384` n `20`; unknown avg `0.1032` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
