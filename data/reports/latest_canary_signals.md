# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T13:37:29.588693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.052` n `229`; crypto_major avg `-0.0754` n `8`; equity avg `-0.0201` n `88`; fx avg `-0.0073` n `6`; index avg `0.0121` n `25`; metal avg `-0.0112` n `20`; unknown avg `-0.0491` n `765`
- 1h: commodity avg `0.1241` n `12`; crypto_alt avg `0.2889` n `229`; crypto_major avg `0.3765` n `8`; equity avg `-0.1` n `88`; fx avg `-0.0008` n `6`; index avg `0.0131` n `25`; metal avg `-0.0477` n `20`; unknown avg `1.1543` n `765`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `1.1852` n `229`; crypto_major avg `1.0876` n `8`; equity avg `0.0532` n `88`; fx avg `-0.0057` n `6`; index avg `0.0492` n `25`; metal avg `-0.1243` n `20`; unknown avg `2.2945` n `765`
- 24h: commodity avg `0.3912` n `12`; crypto_alt avg `1.3792` n `229`; crypto_major avg `1.0905` n `8`; equity avg `-0.8699` n `88`; fx avg `-0.1062` n `6`; index avg `0.0441` n `25`; metal avg `0.3247` n `20`; unknown avg `7.7049` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
