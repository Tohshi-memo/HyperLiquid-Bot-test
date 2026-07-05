# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T08:37:28.082995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0755` n `229`; crypto_major avg `0.022` n `8`; equity avg `0.0462` n `88`; fx avg `0.0022` n `6`; index avg `-0.0004` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0222` n `765`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `0.0487` n `229`; crypto_major avg `0.0953` n `8`; equity avg `0.0542` n `88`; fx avg `0.0` n `6`; index avg `-0.0049` n `25`; metal avg `0.0217` n `20`; unknown avg `0.0014` n `765`
- 4h: commodity avg `0.0351` n `12`; crypto_alt avg `-0.1811` n `229`; crypto_major avg `-0.0313` n `8`; equity avg `0.0674` n `88`; fx avg `0.0115` n `6`; index avg `0.0336` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.1225` n `731`
- 24h: commodity avg `0.0906` n `12`; crypto_alt avg `-0.583` n `229`; crypto_major avg `-0.8008` n `8`; equity avg `0.2301` n `88`; fx avg `0.0149` n `6`; index avg `0.0482` n `25`; metal avg `0.0771` n `20`; unknown avg `-1.3446` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
