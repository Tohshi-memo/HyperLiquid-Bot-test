# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T02:22:28.655361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0386` n `230`; crypto_major avg `-0.0985` n `8`; equity avg `0.1325` n `94`; fx avg `-0.0236` n `6`; index avg `0.0274` n `25`; metal avg `0.0345` n `20`; unknown avg `-0.0861` n `768`
- 1h: commodity avg `-0.0194` n `12`; crypto_alt avg `0.4381` n `230`; crypto_major avg `0.302` n `8`; equity avg `0.2703` n `94`; fx avg `-0.0326` n `6`; index avg `0.0253` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.11` n `768`
- 4h: commodity avg `-0.0681` n `12`; crypto_alt avg `-0.003` n `230`; crypto_major avg `-0.3041` n `8`; equity avg `-0.5097` n `94`; fx avg `-0.0303` n `6`; index avg `-0.2046` n `25`; metal avg `-0.2338` n `20`; unknown avg `-0.1381` n `766`
- 24h: commodity avg `-0.0509` n `12`; crypto_alt avg `0.375` n `230`; crypto_major avg `0.6487` n `8`; equity avg `-1.974` n `93`; fx avg `0.1415` n `6`; index avg `-0.476` n `25`; metal avg `0.0094` n `20`; unknown avg `0.0661` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
