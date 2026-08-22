# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T18:37:25.801133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.1504` n `230`; crypto_major avg `-0.1514` n `8`; equity avg `-0.0142` n `121`; fx avg `0.0063` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.0869` n `794`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `0.1259` n `230`; crypto_major avg `0.4925` n `8`; equity avg `0.025` n `121`; fx avg `0.0111` n `6`; index avg `0.0048` n `25`; metal avg `-0.006` n `20`; unknown avg `0.9705` n `794`
- 4h: commodity avg `0.0221` n `12`; crypto_alt avg `0.8575` n `230`; crypto_major avg `1.3435` n `8`; equity avg `-0.0011` n `121`; fx avg `0.0241` n `6`; index avg `0.0061` n `25`; metal avg `0.0134` n `20`; unknown avg `1.2854` n `794`
- 24h: commodity avg `-0.0839` n `12`; crypto_alt avg `0.9407` n `230`; crypto_major avg `3.6792` n `8`; equity avg `-0.3112` n `121`; fx avg `0.0452` n `6`; index avg `-0.0383` n `25`; metal avg `-0.1252` n `20`; unknown avg `2.8981` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
