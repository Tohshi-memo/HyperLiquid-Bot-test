# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T21:22:28.050653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.0663` n `230`; crypto_major avg `-0.0206` n `8`; equity avg `-0.002` n `121`; fx avg `0.0189` n `6`; index avg `0.0007` n `25`; metal avg `0.0052` n `20`; unknown avg `0.21` n `794`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.6574` n `230`; crypto_major avg `-0.5913` n `8`; equity avg `-0.0294` n `121`; fx avg `0.0222` n `6`; index avg `-0.0024` n `25`; metal avg `0.004` n `20`; unknown avg `0.1692` n `794`
- 4h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.8286` n `230`; crypto_major avg `0.2294` n `8`; equity avg `0.1023` n `121`; fx avg `0.041` n `6`; index avg `-0.0065` n `25`; metal avg `0.0054` n `20`; unknown avg `1.4706` n `794`
- 24h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.667` n `230`; crypto_major avg `2.2389` n `8`; equity avg `-0.3847` n `121`; fx avg `0.0801` n `6`; index avg `-0.0419` n `25`; metal avg `-0.0522` n `20`; unknown avg `3.4063` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
