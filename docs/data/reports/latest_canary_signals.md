# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T03:52:23.604223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0725` n `12`; crypto_alt avg `-0.1097` n `228`; crypto_major avg `-0.0777` n `8`; equity avg `-0.1174` n `74`; fx avg `0.0198` n `6`; index avg `0.0213` n `23`; metal avg `0.1277` n `18`; unknown avg `-0.2629` n `547`
- 1h: commodity avg `-0.0468` n `12`; crypto_alt avg `0.3669` n `228`; crypto_major avg `0.4672` n `8`; equity avg `-0.0931` n `74`; fx avg `0.0149` n `6`; index avg `-0.068` n `23`; metal avg `0.1455` n `18`; unknown avg `-0.2735` n `547`
- 4h: commodity avg `-0.2091` n `12`; crypto_alt avg `-0.5902` n `228`; crypto_major avg `-0.8492` n `8`; equity avg `-0.4299` n `74`; fx avg `0.0106` n `6`; index avg `-0.1321` n `23`; metal avg `-0.7824` n `18`; unknown avg `-0.5331` n `547`
- 24h: commodity avg `-0.4983` n `12`; crypto_alt avg `0.0523` n `228`; crypto_major avg `-2.5006` n `8`; equity avg `-3.1` n `74`; fx avg `0.1406` n `6`; index avg `-1.2981` n `23`; metal avg `-2.7999` n `18`; unknown avg `-0.45` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0435`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0384`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0378`, n `668`, weak_sample_signal
