# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T08:22:29.093244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `-0.0379` n `234`; crypto_major avg `-0.03` n `8`; equity avg `-0.1518` n `140`; fx avg `-0.0212` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0564` n `20`; unknown avg `-0.0278` n `944`
- 1h: commodity avg `-0.0367` n `12`; crypto_alt avg `0.138` n `234`; crypto_major avg `0.1249` n `8`; equity avg `-0.4053` n `140`; fx avg `-0.0262` n `6`; index avg `-0.0648` n `26`; metal avg `-0.1643` n `20`; unknown avg `1.0269` n `936`
- 4h: commodity avg `-0.0355` n `12`; crypto_alt avg `-0.1117` n `234`; crypto_major avg `-0.6561` n `8`; equity avg `-0.9081` n `140`; fx avg `-0.0085` n `6`; index avg `-0.1469` n `26`; metal avg `-0.2706` n `20`; unknown avg `8.9986` n `908`
- 24h: commodity avg `-0.1371` n `12`; crypto_alt avg `2.3826` n `234`; crypto_major avg `3.1247` n `8`; equity avg `0.552` n `140`; fx avg `-0.1715` n `6`; index avg `0.175` n `26`; metal avg `-0.3615` n `20`; unknown avg `1125.8635` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
