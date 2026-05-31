# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T22:37:18.767633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1547` n `12`; crypto_alt avg `0.1318` n `228`; crypto_major avg `0.2028` n `8`; equity avg `0.0384` n `69`; fx avg `0.0` n `6`; index avg `0.0751` n `23`; metal avg `0.0496` n `18`; unknown avg `0.6905` n `421`
- 1h: commodity avg `0.4835` n `12`; crypto_alt avg `0.7706` n `228`; crypto_major avg `0.5069` n `8`; equity avg `-0.052` n `69`; fx avg `-0.0002` n `6`; index avg `0.1386` n `23`; metal avg `-0.0217` n `18`; unknown avg `0.7328` n `421`
- 4h: commodity avg `0.2517` n `12`; crypto_alt avg `1.6505` n `228`; crypto_major avg `1.1077` n `8`; equity avg `0.0841` n `69`; fx avg `-0.0184` n `6`; index avg `0.2491` n `23`; metal avg `-0.0218` n `18`; unknown avg `1.5779` n `421`
- 24h: commodity avg `0.8417` n `12`; crypto_alt avg `1.1227` n `228`; crypto_major avg `0.9118` n `8`; equity avg `0.8272` n `69`; fx avg `-0.0361` n `6`; index avg `0.3973` n `23`; metal avg `-0.1386` n `18`; unknown avg `1.9052` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3177`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2253`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
