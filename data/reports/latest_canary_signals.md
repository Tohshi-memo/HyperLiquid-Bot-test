# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T16:37:26.499353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0491` n `12`; crypto_alt avg `0.0741` n `228`; crypto_major avg `0.0302` n `8`; equity avg `-0.0104` n `88`; fx avg `-0.005` n `6`; index avg `-0.0143` n `23`; metal avg `0.0007` n `20`; unknown avg `-0.0562` n `764`
- 1h: commodity avg `-0.0671` n `12`; crypto_alt avg `-0.0009` n `228`; crypto_major avg `-0.2054` n `8`; equity avg `-0.0866` n `88`; fx avg `-0.005` n `6`; index avg `-0.0264` n `23`; metal avg `-0.0143` n `20`; unknown avg `0.0781` n `764`
- 4h: commodity avg `-0.1047` n `12`; crypto_alt avg `0.9371` n `228`; crypto_major avg `0.9223` n `8`; equity avg `0.06` n `88`; fx avg `0.0023` n `6`; index avg `-0.007` n `23`; metal avg `0.0065` n `20`; unknown avg `0.1391` n `764`
- 24h: commodity avg `0.2024` n `12`; crypto_alt avg `0.5221` n `228`; crypto_major avg `0.3744` n `8`; equity avg `0.4207` n `87`; fx avg `0.0876` n `6`; index avg `-0.1414` n `23`; metal avg `-0.051` n `20`; unknown avg `0.3496` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
