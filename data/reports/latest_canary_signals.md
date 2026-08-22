# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T15:34:32.881277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.5576` n `230`; crypto_major avg `0.5494` n `8`; equity avg `0.0152` n `121`; fx avg `0.003` n `6`; index avg `-0.0005` n `25`; metal avg `0.0067` n `20`; unknown avg `0.4079` n `794`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.136` n `230`; crypto_major avg `0.0953` n `8`; equity avg `-0.0765` n `121`; fx avg `0.0041` n `6`; index avg `0.0062` n `25`; metal avg `0.0081` n `20`; unknown avg `0.3242` n `794`
- 4h: commodity avg `-0.0669` n `12`; crypto_alt avg `-0.5585` n `230`; crypto_major avg `-0.2226` n `8`; equity avg `-0.037` n `121`; fx avg `-0.0244` n `6`; index avg `-0.0039` n `25`; metal avg `0.0269` n `20`; unknown avg `0.3374` n `794`
- 24h: commodity avg `-0.1023` n `12`; crypto_alt avg `0.0349` n `230`; crypto_major avg `2.1821` n `8`; equity avg `-0.5553` n `121`; fx avg `0.0565` n `6`; index avg `-0.0828` n `25`; metal avg `-0.0759` n `20`; unknown avg `2.0661` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
