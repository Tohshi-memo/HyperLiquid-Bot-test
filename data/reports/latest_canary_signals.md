# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T08:37:30.939740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.122` n `228`; crypto_major avg `-0.0686` n `8`; equity avg `0.0117` n `88`; fx avg `-0.0145` n `6`; index avg `-0.004` n `23`; metal avg `0.0061` n `20`; unknown avg `0.1594` n `764`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `-0.2499` n `228`; crypto_major avg `-0.0408` n `8`; equity avg `0.078` n `88`; fx avg `-0.0266` n `6`; index avg `-0.0058` n `23`; metal avg `0.005` n `20`; unknown avg `0.183` n `764`
- 4h: commodity avg `0.0316` n `12`; crypto_alt avg `-0.502` n `228`; crypto_major avg `-0.2622` n `8`; equity avg `0.1822` n `88`; fx avg `0.0116` n `6`; index avg `-0.0007` n `23`; metal avg `-0.0194` n `20`; unknown avg `-0.1294` n `716`
- 24h: commodity avg `0.1144` n `12`; crypto_alt avg `0.8954` n `228`; crypto_major avg `0.7487` n `8`; equity avg `1.5874` n `87`; fx avg `0.0178` n `6`; index avg `0.0265` n `23`; metal avg `0.5978` n `20`; unknown avg `0.0095` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
