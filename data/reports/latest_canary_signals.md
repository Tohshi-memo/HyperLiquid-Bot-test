# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T23:52:29.111092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `0.0992` n `228`; crypto_major avg `0.0143` n `8`; equity avg `0.0245` n `88`; fx avg `-0.0107` n `6`; index avg `0.0005` n `23`; metal avg `0.0022` n `20`; unknown avg `58.2109` n `764`
- 1h: commodity avg `0.0936` n `12`; crypto_alt avg `-0.1214` n `228`; crypto_major avg `-0.4078` n `8`; equity avg `-0.0542` n `88`; fx avg `-0.014` n `6`; index avg `-0.0116` n `23`; metal avg `-0.0074` n `20`; unknown avg `-0.2853` n `764`
- 4h: commodity avg `0.1727` n `12`; crypto_alt avg `-0.1124` n `228`; crypto_major avg `-0.4555` n `8`; equity avg `0.0397` n `88`; fx avg `-0.0042` n `6`; index avg `-0.0394` n `23`; metal avg `0.0098` n `20`; unknown avg `-0.5949` n `764`
- 24h: commodity avg `0.1663` n `12`; crypto_alt avg `-0.7651` n `228`; crypto_major avg `-1.216` n `8`; equity avg `0.2457` n `88`; fx avg `0.0328` n `6`; index avg `-0.0675` n `23`; metal avg `-0.0764` n `20`; unknown avg `-0.9256` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
