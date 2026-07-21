# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T12:52:27.710112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `-0.015` n `230`; crypto_major avg `0.0085` n `8`; equity avg `0.1283` n `98`; fx avg `-0.0052` n `6`; index avg `0.0156` n `25`; metal avg `0.0218` n `20`; unknown avg `0.0873` n `771`
- 1h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0928` n `230`; crypto_major avg `0.0869` n `8`; equity avg `0.0722` n `98`; fx avg `-0.0059` n `6`; index avg `0.0128` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.0395` n `771`
- 4h: commodity avg `0.2779` n `12`; crypto_alt avg `-0.0438` n `230`; crypto_major avg `0.016` n `8`; equity avg `-0.1103` n `98`; fx avg `-0.0176` n `6`; index avg `0.0255` n `25`; metal avg `-0.0479` n `20`; unknown avg `0.0687` n `771`
- 24h: commodity avg `0.3425` n `12`; crypto_alt avg `1.9022` n `230`; crypto_major avg `2.1701` n `8`; equity avg `1.2733` n `98`; fx avg `-0.074` n `6`; index avg `0.2017` n `25`; metal avg `0.6287` n `20`; unknown avg `0.1318` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.089`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
