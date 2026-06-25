# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T08:37:27.000525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1071` n `12`; crypto_alt avg `-0.0374` n `228`; crypto_major avg `-0.0992` n `8`; equity avg `0.0049` n `86`; fx avg `0.0248` n `6`; index avg `0.0134` n `23`; metal avg `0.0103` n `20`; unknown avg `0.0036` n `765`
- 1h: commodity avg `-0.0481` n `12`; crypto_alt avg `0.1523` n `228`; crypto_major avg `-0.3612` n `8`; equity avg `0.0253` n `86`; fx avg `0.0071` n `6`; index avg `0.0029` n `23`; metal avg `0.2933` n `20`; unknown avg `0.0346` n `765`
- 4h: commodity avg `0.0565` n `12`; crypto_alt avg `1.251` n `228`; crypto_major avg `1.3067` n `8`; equity avg `0.4762` n `86`; fx avg `-0.0505` n `6`; index avg `0.0673` n `23`; metal avg `0.1219` n `20`; unknown avg `0.1894` n `733`
- 24h: commodity avg `-0.3085` n `12`; crypto_alt avg `-0.9818` n `228`; crypto_major avg `-0.8608` n `8`; equity avg `0.0476` n `86`; fx avg `-0.013` n `6`; index avg `0.501` n `23`; metal avg `-1.3877` n `20`; unknown avg `-0.7191` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
