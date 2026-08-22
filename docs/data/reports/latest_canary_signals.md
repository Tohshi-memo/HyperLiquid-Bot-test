# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T12:22:26.560824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.2226` n `230`; crypto_major avg `0.2944` n `8`; equity avg `0.0185` n `121`; fx avg `0.0004` n `6`; index avg `0.0016` n `25`; metal avg `-0.003` n `20`; unknown avg `0.0732` n `794`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `1.3169` n `230`; crypto_major avg `1.4159` n `8`; equity avg `0.1186` n `121`; fx avg `-0.0075` n `6`; index avg `0.0126` n `25`; metal avg `0.0372` n `20`; unknown avg `0.3364` n `794`
- 4h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.6928` n `230`; crypto_major avg `-0.4395` n `8`; equity avg `-0.0454` n `121`; fx avg `0.0284` n `6`; index avg `0.0039` n `25`; metal avg `0.0228` n `20`; unknown avg `0.0963` n `794`
- 24h: commodity avg `-0.0515` n `12`; crypto_alt avg `2.4198` n `230`; crypto_major avg `4.9111` n `8`; equity avg `-0.8008` n `121`; fx avg `0.039` n `6`; index avg `-0.1143` n `25`; metal avg `-0.1176` n `20`; unknown avg `1.607` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
