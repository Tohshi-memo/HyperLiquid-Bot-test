# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T10:49:49.349898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.0109` n `229`; crypto_major avg `0.141` n `8`; equity avg `0.0558` n `88`; fx avg `0.0012` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0189` n `765`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.2902` n `229`; crypto_major avg `0.4144` n `8`; equity avg `0.1146` n `88`; fx avg `0.0012` n `6`; index avg `0.0058` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0726` n `765`
- 4h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.196` n `229`; crypto_major avg `0.0054` n `8`; equity avg `0.0471` n `88`; fx avg `0.0027` n `6`; index avg `-0.0092` n `25`; metal avg `0.0222` n `20`; unknown avg `-0.23` n `765`
- 24h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.8007` n `229`; crypto_major avg `-0.6352` n `8`; equity avg `0.1891` n `88`; fx avg `0.0449` n `6`; index avg `0.0314` n `25`; metal avg `0.077` n `20`; unknown avg `-1.2611` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
