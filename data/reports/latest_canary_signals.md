# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T14:22:25.283309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.1935` n `230`; crypto_major avg `0.2431` n `8`; equity avg `0.0109` n `121`; fx avg `-0.0015` n `6`; index avg `0.0021` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0514` n `794`
- 1h: commodity avg `-0.0285` n `12`; crypto_alt avg `-0.2686` n `230`; crypto_major avg `-0.1681` n `8`; equity avg `0.0077` n `121`; fx avg `-0.0276` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.006` n `794`
- 4h: commodity avg `-0.0767` n `12`; crypto_alt avg `1.2994` n `230`; crypto_major avg `1.5177` n `8`; equity avg `0.1178` n `121`; fx avg `-0.0209` n `6`; index avg `0.0072` n `25`; metal avg `0.0304` n `20`; unknown avg `0.4204` n `794`
- 24h: commodity avg `-0.0552` n `12`; crypto_alt avg `0.5809` n `230`; crypto_major avg `3.0025` n `8`; equity avg `-0.115` n `121`; fx avg `0.0346` n `6`; index avg `-0.0035` n `25`; metal avg `-0.1698` n `20`; unknown avg `1.3658` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
