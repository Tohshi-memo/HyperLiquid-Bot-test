# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T21:37:29.033370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `13`; crypto_alt avg `0.0388` n `239`; crypto_major avg `0.1217` n `8`; equity avg `0.0582` n `168`; fx avg `-0.0019` n `6`; index avg `0.0062` n `27`; metal avg `0.0081` n `20`; unknown avg `6.9363` n `1263`
- 1h: commodity avg `-0.0045` n `13`; crypto_alt avg `0.1175` n `239`; crypto_major avg `0.14` n `8`; equity avg `0.1892` n `168`; fx avg `-0.0038` n `6`; index avg `0.0147` n `27`; metal avg `0.0276` n `20`; unknown avg `0.8394` n `1199`
- 4h: commodity avg `0.0322` n `13`; crypto_alt avg `0.7722` n `239`; crypto_major avg `1.2292` n `8`; equity avg `0.5943` n `168`; fx avg `-0.0058` n `6`; index avg `0.0468` n `27`; metal avg `0.0664` n `20`; unknown avg `48.1038` n `1181`
- 24h: commodity avg `0.0899` n `13`; crypto_alt avg `1.7765` n `239`; crypto_major avg `1.0072` n `8`; equity avg `1.3206` n `168`; fx avg `-0.0273` n `6`; index avg `0.0812` n `27`; metal avg `0.157` n `20`; unknown avg `19.1883` n `1019`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
