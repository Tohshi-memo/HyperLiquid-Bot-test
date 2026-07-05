# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T23:07:30.316452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.1725` n `229`; crypto_major avg `0.1456` n `8`; equity avg `0.0733` n `88`; fx avg `-0.0038` n `6`; index avg `0.0356` n `25`; metal avg `0.0164` n `20`; unknown avg `0.0159` n `765`
- 1h: commodity avg `-0.1182` n `12`; crypto_alt avg `0.2641` n `229`; crypto_major avg `0.4594` n `8`; equity avg `0.2076` n `88`; fx avg `0.0012` n `6`; index avg `0.0522` n `25`; metal avg `0.1181` n `20`; unknown avg `0.7446` n `765`
- 4h: commodity avg `-0.1385` n `12`; crypto_alt avg `0.7438` n `229`; crypto_major avg `1.1699` n `8`; equity avg `0.2263` n `88`; fx avg `0.0859` n `6`; index avg `0.0103` n `25`; metal avg `0.1794` n `20`; unknown avg `1.2348` n `765`
- 24h: commodity avg `-0.1562` n `12`; crypto_alt avg `0.1255` n `229`; crypto_major avg `0.7797` n `8`; equity avg `0.4807` n `88`; fx avg `0.0192` n `6`; index avg `0.0884` n `25`; metal avg `0.1936` n `20`; unknown avg `1.1529` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
