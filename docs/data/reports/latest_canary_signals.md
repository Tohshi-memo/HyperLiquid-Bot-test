# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T11:37:26.861022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.1011` n `229`; crypto_major avg `-0.1775` n `8`; equity avg `-0.0302` n `88`; fx avg `0.0022` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0625` n `765`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `0.3816` n `229`; crypto_major avg `0.285` n `8`; equity avg `0.0621` n `88`; fx avg `0.0127` n `6`; index avg `0.0126` n `25`; metal avg `0.0016` n `20`; unknown avg `0.439` n `765`
- 4h: commodity avg `-0.088` n `12`; crypto_alt avg `0.9149` n `229`; crypto_major avg `0.8629` n `8`; equity avg `0.2513` n `88`; fx avg `0.0702` n `6`; index avg `0.02` n `25`; metal avg `-0.0825` n `20`; unknown avg `1.1269` n `755`
- 24h: commodity avg `0.5837` n `12`; crypto_alt avg `1.9191` n `229`; crypto_major avg `2.2213` n `8`; equity avg `0.1829` n `88`; fx avg `-0.0712` n `6`; index avg `0.2317` n `25`; metal avg `1.1747` n `20`; unknown avg `6.1816` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
