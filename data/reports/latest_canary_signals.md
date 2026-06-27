# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T16:07:27.238010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `0.1425` n `228`; crypto_major avg `0.0245` n `8`; equity avg `-0.0259` n `88`; fx avg `0.0101` n `6`; index avg `-0.0151` n `23`; metal avg `-0.0062` n `20`; unknown avg `0.0347` n `764`
- 1h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.4217` n `228`; crypto_major avg `0.2055` n `8`; equity avg `-0.033` n `88`; fx avg `-0.004` n `6`; index avg `0.0043` n `23`; metal avg `0.0066` n `20`; unknown avg `0.1341` n `764`
- 4h: commodity avg `-0.1055` n `12`; crypto_alt avg `1.087` n `228`; crypto_major avg `1.1715` n `8`; equity avg `0.1117` n `88`; fx avg `0.0043` n `6`; index avg `0.021` n `23`; metal avg `0.0066` n `20`; unknown avg `0.3239` n `764`
- 24h: commodity avg `0.2061` n `12`; crypto_alt avg `1.0159` n `228`; crypto_major avg `0.7419` n `8`; equity avg `0.5453` n `87`; fx avg `0.0696` n `6`; index avg `-0.0899` n `23`; metal avg `-0.0508` n `20`; unknown avg `0.2352` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
