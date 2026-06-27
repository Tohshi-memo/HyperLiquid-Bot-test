# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T01:48:40.807666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0154` n `228`; crypto_major avg `0.057` n `8`; equity avg `-0.0001` n `88`; fx avg `-0.0007` n `6`; index avg `0.0033` n `23`; metal avg `0.0001` n `20`; unknown avg `0.1693` n `764`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `-0.1143` n `228`; crypto_major avg `-0.0862` n `8`; equity avg `0.159` n `88`; fx avg `0.0042` n `6`; index avg `0.011` n `23`; metal avg `0.0164` n `20`; unknown avg `-0.4399` n `764`
- 4h: commodity avg `0.0562` n `12`; crypto_alt avg `-0.1002` n `228`; crypto_major avg `-0.171` n `8`; equity avg `0.2441` n `88`; fx avg `-0.0274` n `6`; index avg `0.0337` n `23`; metal avg `0.062` n `20`; unknown avg `-0.1974` n `748`
- 24h: commodity avg `-0.1892` n `12`; crypto_alt avg `1.9461` n `228`; crypto_major avg `1.737` n `8`; equity avg `0.7002` n `87`; fx avg `-0.027` n `6`; index avg `-0.1009` n `23`; metal avg `1.0642` n `20`; unknown avg `0.0662` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
