# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T19:38:16.341056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0197` n `230`; crypto_major avg `0.0489` n `8`; equity avg `0.1408` n `114`; fx avg `-0.002` n `6`; index avg `0.0079` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.1042` n `792`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.0703` n `230`; crypto_major avg `-0.168` n `8`; equity avg `-0.1552` n `114`; fx avg `0.0044` n `6`; index avg `-0.0194` n `25`; metal avg `0.0642` n `20`; unknown avg `0.0919` n `792`
- 4h: commodity avg `0.3912` n `12`; crypto_alt avg `-0.1511` n `230`; crypto_major avg `-0.1429` n `8`; equity avg `-0.4206` n `114`; fx avg `0.0102` n `6`; index avg `-0.1361` n `25`; metal avg `-0.0966` n `20`; unknown avg `0.1364` n `792`
- 24h: commodity avg `0.3014` n `12`; crypto_alt avg `-0.108` n `230`; crypto_major avg `0.7011` n `8`; equity avg `1.1529` n `114`; fx avg `0.0151` n `6`; index avg `0.062` n `25`; metal avg `0.1877` n `20`; unknown avg `0.2948` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
