# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T14:04:18.752064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.1101` n `228`; crypto_major avg `-0.0922` n `8`; equity avg `-0.0425` n `88`; fx avg `-0.0007` n `6`; index avg `0.0064` n `23`; metal avg `0.0024` n `20`; unknown avg `-0.0319` n `764`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `0.139` n `228`; crypto_major avg `0.1606` n `8`; equity avg `0.0274` n `88`; fx avg `-0.002` n `6`; index avg `-0.0075` n `23`; metal avg `0.0066` n `20`; unknown avg `-0.0028` n `764`
- 4h: commodity avg `0.1304` n `12`; crypto_alt avg `0.3217` n `228`; crypto_major avg `0.4019` n `8`; equity avg `0.0932` n `88`; fx avg `0.0197` n `6`; index avg `-0.0124` n `23`; metal avg `0.014` n `20`; unknown avg `0.2096` n `764`
- 24h: commodity avg `0.3559` n `12`; crypto_alt avg `1.4571` n `228`; crypto_major avg `1.2342` n `8`; equity avg `0.8869` n `87`; fx avg `0.0185` n `6`; index avg `-0.0624` n `23`; metal avg `0.064` n `20`; unknown avg `0.2908` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
