# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T21:07:32.666609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0834` n `12`; crypto_alt avg `0.157` n `228`; crypto_major avg `0.1674` n `8`; equity avg `0.0164` n `88`; fx avg `0.0031` n `6`; index avg `0.0019` n `23`; metal avg `0.0066` n `20`; unknown avg `0.1192` n `764`
- 1h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.159` n `228`; crypto_major avg `0.2099` n `8`; equity avg `0.0652` n `88`; fx avg `0.0023` n `6`; index avg `0.0244` n `23`; metal avg `0.0146` n `20`; unknown avg `-0.022` n `764`
- 4h: commodity avg `-0.0603` n `12`; crypto_alt avg `-0.664` n `228`; crypto_major avg `-0.7703` n `8`; equity avg `0.0057` n `88`; fx avg `0.0046` n `6`; index avg `0.0126` n `23`; metal avg `-0.0438` n `20`; unknown avg `-0.2542` n `764`
- 24h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.0171` n `228`; crypto_major avg `0.0377` n `8`; equity avg `0.6457` n `88`; fx avg `0.0477` n `6`; index avg `0.0452` n `23`; metal avg `0.0103` n `20`; unknown avg `-0.2108` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
