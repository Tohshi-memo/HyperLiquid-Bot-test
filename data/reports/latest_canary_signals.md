# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T01:07:28.512045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0704` n `13`; crypto_alt avg `-0.0569` n `239`; crypto_major avg `0.1287` n `8`; equity avg `-0.1082` n `168`; fx avg `-0.0164` n `6`; index avg `-0.0113` n `27`; metal avg `-0.0098` n `20`; unknown avg `18.9775` n `1257`
- 1h: commodity avg `0.0713` n `13`; crypto_alt avg `0.3871` n `239`; crypto_major avg `0.2303` n `8`; equity avg `0.6622` n `168`; fx avg `-0.0242` n `6`; index avg `0.0849` n `27`; metal avg `-0.0947` n `20`; unknown avg `235.75` n `1255`
- 4h: commodity avg `0.0448` n `13`; crypto_alt avg `0.7686` n `239`; crypto_major avg `0.1742` n `8`; equity avg `1.246` n `168`; fx avg `-0.0368` n `6`; index avg `0.1086` n `27`; metal avg `-0.0132` n `20`; unknown avg `12.8136` n `1185`
- 24h: commodity avg `0.4472` n `13`; crypto_alt avg `3.6314` n `239`; crypto_major avg `2.174` n `8`; equity avg `1.7909` n `168`; fx avg `-0.0162` n `6`; index avg `0.1699` n `27`; metal avg `0.3459` n `20`; unknown avg `768.8943` n `1019`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
