# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T08:22:30.841769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `0.1602` n `230`; crypto_major avg `0.0835` n `8`; equity avg `-0.1707` n `114`; fx avg `0.0251` n `6`; index avg `-0.003` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.017` n `795`
- 1h: commodity avg `0.0968` n `12`; crypto_alt avg `-0.084` n `230`; crypto_major avg `-0.3958` n `8`; equity avg `-0.8481` n `114`; fx avg `0.0184` n `6`; index avg `-0.1149` n `25`; metal avg `-0.1481` n `20`; unknown avg `0.1101` n `795`
- 4h: commodity avg `0.007` n `12`; crypto_alt avg `0.4389` n `230`; crypto_major avg `0.0928` n `8`; equity avg `-0.9633` n `114`; fx avg `0.012` n `6`; index avg `-0.166` n `25`; metal avg `-0.0597` n `20`; unknown avg `0.0057` n `761`
- 24h: commodity avg `0.7203` n `12`; crypto_alt avg `-0.8762` n `230`; crypto_major avg `0.1163` n `8`; equity avg `-2.5688` n `114`; fx avg `-0.0039` n `6`; index avg `-0.5268` n `25`; metal avg `-0.3107` n `20`; unknown avg `0.0127` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
