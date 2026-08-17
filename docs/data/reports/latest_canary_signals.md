# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T22:45:20.692415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `-0.0192` n `8`; equity avg `-0.0053` n `114`; fx avg `0.0069` n `6`; index avg `0.0025` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.025` n `793`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.368` n `230`; crypto_major avg `-0.0906` n `8`; equity avg `0.0782` n `114`; fx avg `0.021` n `6`; index avg `0.0091` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0358` n `792`
- 4h: commodity avg `0.1655` n `12`; crypto_alt avg `-0.4541` n `230`; crypto_major avg `-0.1699` n `8`; equity avg `-0.1607` n `114`; fx avg `0.0139` n `6`; index avg `-0.0155` n `25`; metal avg `0.005` n `20`; unknown avg `-0.013` n `792`
- 24h: commodity avg `0.5808` n `12`; crypto_alt avg `0.457` n `230`; crypto_major avg `1.4467` n `8`; equity avg `1.2222` n `114`; fx avg `0.0351` n `6`; index avg `0.0608` n `25`; metal avg `0.1138` n `20`; unknown avg `0.2779` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
