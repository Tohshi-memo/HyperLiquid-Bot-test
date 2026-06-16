# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T14:07:51.122068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0452` n `12`; crypto_alt avg `0.0246` n `228`; crypto_major avg `0.0982` n `8`; equity avg `-0.3192` n `77`; fx avg `-0.0026` n `6`; index avg `-0.1065` n `23`; metal avg `0.0035` n `18`; unknown avg `0.14` n `687`
- 1h: commodity avg `0.4887` n `12`; crypto_alt avg `-0.6897` n `228`; crypto_major avg `-0.733` n `8`; equity avg `0.3374` n `77`; fx avg `-0.0149` n `6`; index avg `0.139` n `23`; metal avg `-0.084` n `18`; unknown avg `0.3164` n `687`
- 4h: commodity avg `0.115` n `12`; crypto_alt avg `-0.599` n `228`; crypto_major avg `-0.198` n `8`; equity avg `-0.2822` n `77`; fx avg `-0.0176` n `6`; index avg `-0.0025` n `23`; metal avg `0.1381` n `18`; unknown avg `0.6115` n `687`
- 24h: commodity avg `-0.0679` n `12`; crypto_alt avg `-1.1258` n `228`; crypto_major avg `0.829` n `8`; equity avg `1.1547` n `77`; fx avg `-0.1052` n `6`; index avg `0.2404` n `23`; metal avg `-0.3488` n `18`; unknown avg `0.5407` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
