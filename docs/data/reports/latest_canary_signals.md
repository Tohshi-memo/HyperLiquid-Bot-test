# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T13:43:13.139061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0652` n `230`; crypto_major avg `-0.0844` n `8`; equity avg `0.0004` n `121`; fx avg `-0.0042` n `6`; index avg `-0.0048` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0101` n `794`
- 1h: commodity avg `-0.0589` n `12`; crypto_alt avg `-0.3569` n `230`; crypto_major avg `-0.4029` n `8`; equity avg `-0.0115` n `121`; fx avg `-0.0049` n `6`; index avg `-0.0148` n `25`; metal avg `0.0143` n `20`; unknown avg `-0.0278` n `794`
- 4h: commodity avg `-0.0757` n `12`; crypto_alt avg `-0.6617` n `230`; crypto_major avg `-0.4841` n `8`; equity avg `-0.0726` n `121`; fx avg `0.01` n `6`; index avg `-0.0027` n `25`; metal avg `0.0319` n `20`; unknown avg `0.0387` n `794`
- 24h: commodity avg `-0.1279` n `12`; crypto_alt avg `1.569` n `230`; crypto_major avg `3.3666` n `8`; equity avg `-0.5857` n `121`; fx avg `0.0723` n `6`; index avg `-0.0116` n `25`; metal avg `-0.1053` n `20`; unknown avg `0.8194` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
