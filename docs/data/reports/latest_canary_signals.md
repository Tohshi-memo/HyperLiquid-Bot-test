# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T18:52:32.023630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.5863` n `230`; crypto_major avg `-0.4495` n `8`; equity avg `-0.0001` n `121`; fx avg `0.0048` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0143` n `794`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.7611` n `230`; crypto_major avg `-0.305` n `8`; equity avg `-0.0062` n `121`; fx avg `0.013` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.2229` n `794`
- 4h: commodity avg `0.0256` n `12`; crypto_alt avg `0.636` n `230`; crypto_major avg `1.136` n `8`; equity avg `0.0334` n `121`; fx avg `0.0307` n `6`; index avg `-0.0006` n `25`; metal avg `0.0124` n `20`; unknown avg `1.1977` n `794`
- 24h: commodity avg `-0.0827` n `12`; crypto_alt avg `1.0723` n `230`; crypto_major avg `3.8369` n `8`; equity avg `-0.406` n `121`; fx avg `0.049` n `6`; index avg `-0.0515` n `25`; metal avg `-0.139` n `20`; unknown avg `2.8899` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
