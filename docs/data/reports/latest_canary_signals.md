# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T20:52:28.560695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `13`; crypto_alt avg `0.0214` n `236`; crypto_major avg `-0.1248` n `8`; equity avg `-0.1262` n `151`; fx avg `0.0023` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0075` n `20`; unknown avg `6.943` n `1136`
- 1h: commodity avg `-0.0369` n `13`; crypto_alt avg `0.1257` n `236`; crypto_major avg `-0.2113` n `8`; equity avg `-0.306` n `151`; fx avg `0.0052` n `6`; index avg `-0.0579` n `26`; metal avg `-0.0166` n `20`; unknown avg `1.8313` n `1086`
- 4h: commodity avg `0.0084` n `13`; crypto_alt avg `-0.3326` n `236`; crypto_major avg `-0.3977` n `8`; equity avg `-0.8626` n `151`; fx avg `0.0263` n `6`; index avg `-0.1359` n `26`; metal avg `-0.0206` n `20`; unknown avg `-0.8287` n `1086`
- 24h: commodity avg `-0.1477` n `13`; crypto_alt avg `-2.6189` n `236`; crypto_major avg `-2.1877` n `8`; equity avg `-4.3753` n `151`; fx avg `-0.1274` n `6`; index avg `-0.6066` n `26`; metal avg `-0.8473` n `20`; unknown avg `1305.1295` n `948`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0851`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0656`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0621`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0519`, n `666`, weak_sample_signal
