# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T05:52:29.975938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0442` n `12`; crypto_alt avg `-0.1721` n `230`; crypto_major avg `-0.1449` n `8`; equity avg `-0.0721` n `121`; fx avg `-0.0142` n `6`; index avg `-0.0135` n `25`; metal avg `0.0062` n `20`; unknown avg `5.3605` n `792`
- 1h: commodity avg `0.0604` n `12`; crypto_alt avg `-0.1094` n `230`; crypto_major avg `0.0081` n `8`; equity avg `-0.1964` n `121`; fx avg `0.0107` n `6`; index avg `-0.0361` n `25`; metal avg `-0.1003` n `20`; unknown avg `-0.1565` n `792`
- 4h: commodity avg `0.023` n `12`; crypto_alt avg `-0.3726` n `230`; crypto_major avg `-0.22` n `8`; equity avg `-0.2403` n `121`; fx avg `0.0244` n `6`; index avg `-0.0504` n `25`; metal avg `-0.0114` n `20`; unknown avg `-0.1106` n `792`
- 24h: commodity avg `-0.0353` n `12`; crypto_alt avg `5.3483` n `230`; crypto_major avg `9.8626` n `8`; equity avg `1.3908` n `120`; fx avg `0.1023` n `6`; index avg `0.3383` n `25`; metal avg `1.0528` n `20`; unknown avg `1.7115` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
