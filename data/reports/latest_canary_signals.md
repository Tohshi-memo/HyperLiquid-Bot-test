# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T01:22:30.781528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `-0.418` n `233`; crypto_major avg `-0.3998` n `8`; equity avg `-0.1431` n `134`; fx avg `0.0226` n `6`; index avg `-0.0218` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.9039` n `797`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.251` n `233`; crypto_major avg `-0.18` n `8`; equity avg `-0.4566` n `134`; fx avg `0.0151` n `6`; index avg `-0.1045` n `26`; metal avg `0.0219` n `20`; unknown avg `8.538` n `789`
- 4h: commodity avg `-0.0558` n `12`; crypto_alt avg `-1.7046` n `233`; crypto_major avg `-0.8207` n `8`; equity avg `-0.5438` n `134`; fx avg `-0.0012` n `6`; index avg `-0.0724` n `26`; metal avg `0.0143` n `20`; unknown avg `0.4938` n `729`
- 24h: commodity avg `0.0466` n `12`; crypto_alt avg `-3.1417` n `233`; crypto_major avg `-2.1939` n `8`; equity avg `-1.4001` n `134`; fx avg `-0.0068` n `6`; index avg `-0.2917` n `26`; metal avg `0.4426` n `20`; unknown avg `0.9457` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
