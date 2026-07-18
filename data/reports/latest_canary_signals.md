# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T08:37:26.064144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `12`; crypto_alt avg `-0.0078` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `0.0047` n `96`; fx avg `-0.0124` n `6`; index avg `0.0264` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0122` n `769`
- 1h: commodity avg `0.0084` n `12`; crypto_alt avg `0.07` n `230`; crypto_major avg `0.0759` n `8`; equity avg `-0.034` n `96`; fx avg `-0.0059` n `6`; index avg `0.0453` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0654` n `769`
- 4h: commodity avg `0.0301` n `12`; crypto_alt avg `-0.1042` n `230`; crypto_major avg `0.0328` n `8`; equity avg `-0.0915` n `96`; fx avg `-0.008` n `6`; index avg `0.0052` n `25`; metal avg `0.0206` n `20`; unknown avg `-0.0668` n `737`
- 24h: commodity avg `0.8342` n `12`; crypto_alt avg `0.3463` n `230`; crypto_major avg `0.9521` n `8`; equity avg `1.9731` n `96`; fx avg `0.0012` n `6`; index avg `0.2962` n `25`; metal avg `0.3413` n `20`; unknown avg `0.3211` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
