# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T22:07:28.349154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0714` n `230`; crypto_major avg `-0.114` n `8`; equity avg `-0.1619` n `98`; fx avg `-0.0004` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0117` n `20`; unknown avg `-0.0717` n `771`
- 1h: commodity avg `0.0012` n `12`; crypto_alt avg `0.0359` n `230`; crypto_major avg `-0.0395` n `8`; equity avg `-0.0771` n `98`; fx avg `-0.0037` n `6`; index avg `0.0035` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.0119` n `771`
- 4h: commodity avg `0.1459` n `12`; crypto_alt avg `0.0851` n `230`; crypto_major avg `-0.1827` n `8`; equity avg `0.3687` n `98`; fx avg `-0.0051` n `6`; index avg `-0.0049` n `25`; metal avg `0.0332` n `20`; unknown avg `-0.1777` n `771`
- 24h: commodity avg `0.4497` n `12`; crypto_alt avg `0.9646` n `230`; crypto_major avg `0.6534` n `8`; equity avg `4.3392` n `98`; fx avg `0.0633` n `6`; index avg `0.691` n `25`; metal avg `0.7454` n `20`; unknown avg `0.1387` n `754`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0921`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
