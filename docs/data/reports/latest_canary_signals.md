# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T20:37:25.100872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.0662` n `230`; crypto_major avg `0.0533` n `8`; equity avg `0.0006` n `121`; fx avg `0.0049` n `6`; index avg `0.0011` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0166` n `794`
- 1h: commodity avg `0.0417` n `12`; crypto_alt avg `-0.0228` n `230`; crypto_major avg `0.3902` n `8`; equity avg `0.0746` n `121`; fx avg `0.0099` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.0539` n `794`
- 4h: commodity avg `0.065` n `12`; crypto_alt avg `0.1204` n `230`; crypto_major avg `1.2249` n `8`; equity avg `0.1427` n `121`; fx avg `0.0221` n `6`; index avg `-0.0089` n `25`; metal avg `0.0072` n `20`; unknown avg `1.3324` n `794`
- 24h: commodity avg `0.0311` n `12`; crypto_alt avg `0.7768` n `230`; crypto_major avg `3.8793` n `8`; equity avg `-0.3732` n `121`; fx avg `0.0783` n `6`; index avg `-0.0415` n `25`; metal avg `-0.0659` n `20`; unknown avg `3.2094` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
