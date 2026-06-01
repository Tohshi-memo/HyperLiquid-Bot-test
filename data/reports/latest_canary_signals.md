# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T21:52:19.079880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2713` n `12`; crypto_alt avg `-0.0557` n `228`; crypto_major avg `0.0611` n `8`; equity avg `0.1245` n `69`; fx avg `-0.0153` n `6`; index avg `-0.0558` n `23`; metal avg `0.0507` n `18`; unknown avg `0.1159` n `422`
- 1h: commodity avg `0.1167` n `12`; crypto_alt avg `-0.4753` n `228`; crypto_major avg `-0.2713` n `8`; equity avg `0.0769` n `69`; fx avg `-0.0171` n `6`; index avg `-0.0942` n `23`; metal avg `0.0643` n `18`; unknown avg `-0.1385` n `422`
- 4h: commodity avg `0.5805` n `12`; crypto_alt avg `-0.4701` n `228`; crypto_major avg `-0.0759` n `8`; equity avg `-0.8032` n `69`; fx avg `-0.0158` n `6`; index avg `-0.4423` n `23`; metal avg `-0.2821` n `18`; unknown avg `-0.5431` n `422`
- 24h: commodity avg `0.7299` n `12`; crypto_alt avg `0.0575` n `228`; crypto_major avg `-1.2528` n `8`; equity avg `-0.1089` n `69`; fx avg `0.0489` n `6`; index avg `-0.0821` n `23`; metal avg `-0.0607` n `18`; unknown avg `2.3316` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
