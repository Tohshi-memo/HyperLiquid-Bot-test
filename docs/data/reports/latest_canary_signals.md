# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T04:22:28.209862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1439` n `228`; crypto_major avg `0.0065` n `8`; equity avg `0.0447` n `88`; fx avg `-0.0015` n `6`; index avg `0.0024` n `23`; metal avg `0.0014` n `20`; unknown avg `-0.3587` n `764`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.1117` n `228`; crypto_major avg `0.1868` n `8`; equity avg `0.0062` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0033` n `23`; metal avg `0.0122` n `20`; unknown avg `10.3115` n `764`
- 4h: commodity avg `-0.0445` n `12`; crypto_alt avg `0.4292` n `228`; crypto_major avg `0.5075` n `8`; equity avg `0.1938` n `88`; fx avg `0.0007` n `6`; index avg `0.0257` n `23`; metal avg `0.0206` n `20`; unknown avg `0.9446` n `764`
- 24h: commodity avg `-0.0629` n `12`; crypto_alt avg `2.289` n `228`; crypto_major avg `2.0435` n `8`; equity avg `1.8292` n `87`; fx avg `-0.0116` n `6`; index avg `0.1557` n `23`; metal avg `1.2024` n `20`; unknown avg `-0.0761` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2038`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
