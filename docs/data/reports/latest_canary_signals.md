# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T02:07:26.702799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `0.1056` n `228`; crypto_major avg `0.0878` n `8`; equity avg `-0.0085` n `88`; fx avg `0.0` n `6`; index avg `0.0024` n `23`; metal avg `0.0003` n `20`; unknown avg `0.191` n `764`
- 1h: commodity avg `0.044` n `12`; crypto_alt avg `0.306` n `228`; crypto_major avg `0.3564` n `8`; equity avg `0.0455` n `88`; fx avg `-0.0094` n `6`; index avg `0.0131` n `23`; metal avg `0.0109` n `20`; unknown avg `305.5455` n `764`
- 4h: commodity avg `0.3284` n `12`; crypto_alt avg `0.2966` n `228`; crypto_major avg `0.024` n `8`; equity avg `-0.0779` n `88`; fx avg `-0.0232` n `6`; index avg `-0.0435` n `23`; metal avg `0.0441` n `20`; unknown avg `-0.6599` n `764`
- 24h: commodity avg `0.5861` n `12`; crypto_alt avg `-0.3591` n `228`; crypto_major avg `-0.6674` n `8`; equity avg `0.1045` n `88`; fx avg `-0.0051` n `6`; index avg `-0.1157` n `23`; metal avg `-0.0396` n `20`; unknown avg `-0.4184` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
