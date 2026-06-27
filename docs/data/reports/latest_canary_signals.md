# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T17:37:24.767667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `-0.0106` n `228`; crypto_major avg `0.006` n `8`; equity avg `0.0114` n `88`; fx avg `-0.0013` n `6`; index avg `-0.0003` n `23`; metal avg `-0.0051` n `20`; unknown avg `0.0061` n `764`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.6257` n `228`; crypto_major avg `-0.5165` n `8`; equity avg `-0.0901` n `88`; fx avg `-0.0023` n `6`; index avg `-0.0138` n `23`; metal avg `-0.0362` n `20`; unknown avg `0.2028` n `764`
- 4h: commodity avg `-0.1056` n `12`; crypto_alt avg `0.1553` n `228`; crypto_major avg `0.0269` n `8`; equity avg `-0.0837` n `88`; fx avg `0.0005` n `6`; index avg `-0.0329` n `23`; metal avg `-0.0334` n `20`; unknown avg `0.0515` n `764`
- 24h: commodity avg `0.1613` n `12`; crypto_alt avg `0.0145` n `228`; crypto_major avg `0.2286` n `8`; equity avg `0.3314` n `87`; fx avg `0.0809` n `6`; index avg `-0.1521` n `23`; metal avg `0.0022` n `20`; unknown avg `0.1719` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
