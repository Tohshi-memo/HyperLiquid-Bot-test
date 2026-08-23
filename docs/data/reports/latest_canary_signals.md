# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T02:07:23.487040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.2709` n `230`; crypto_major avg `-0.1354` n `8`; equity avg `0.0042` n `121`; fx avg `0.0114` n `6`; index avg `0.0015` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0526` n `794`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `-1.0021` n `230`; crypto_major avg `-0.4487` n `8`; equity avg `0.0287` n `121`; fx avg `-0.0021` n `6`; index avg `0.0049` n `25`; metal avg `0.0145` n `20`; unknown avg `3.1723` n `794`
- 4h: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0448` n `230`; crypto_major avg `0.7865` n `8`; equity avg `0.1835` n `121`; fx avg `0.0401` n `6`; index avg `0.0223` n `25`; metal avg `0.0334` n `20`; unknown avg `2.8585` n `794`
- 24h: commodity avg `0.082` n `12`; crypto_alt avg `-3.7438` n `230`; crypto_major avg `0.0796` n `8`; equity avg `-0.2281` n `121`; fx avg `0.1111` n `6`; index avg `-0.041` n `25`; metal avg `-0.01` n `20`; unknown avg `3.7907` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
