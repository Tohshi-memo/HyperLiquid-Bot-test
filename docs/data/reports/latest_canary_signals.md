# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T18:22:25.607630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0051` n `229`; crypto_major avg `0.0784` n `8`; equity avg `-0.0186` n `88`; fx avg `0.0016` n `6`; index avg `0.0007` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.0201` n `765`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.0314` n `229`; crypto_major avg `0.146` n `8`; equity avg `0.0284` n `88`; fx avg `0.0089` n `6`; index avg `0.0246` n `25`; metal avg `-0.0087` n `20`; unknown avg `1.7959` n `765`
- 4h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.5695` n `229`; crypto_major avg `0.9289` n `8`; equity avg `0.1823` n `88`; fx avg `-0.0143` n `6`; index avg `0.0098` n `25`; metal avg `-0.0062` n `20`; unknown avg `2.9397` n `765`
- 24h: commodity avg `0.1703` n `12`; crypto_alt avg `2.424` n `229`; crypto_major avg `2.1277` n `8`; equity avg `2.4315` n `88`; fx avg `-0.0493` n `6`; index avg `0.6708` n `25`; metal avg `0.6478` n `20`; unknown avg `11.8807` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
