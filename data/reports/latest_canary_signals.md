# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T02:17:51.770249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `0.2391` n `239`; crypto_major avg `0.2015` n `8`; equity avg `0.2374` n `168`; fx avg `0.005` n `6`; index avg `0.0032` n `27`; metal avg `0.104` n `20`; unknown avg `-0.0232` n `1263`
- 1h: commodity avg `-0.0611` n `13`; crypto_alt avg `0.3773` n `239`; crypto_major avg `0.3381` n `8`; equity avg `-0.1163` n `168`; fx avg `-0.0349` n `6`; index avg `-0.0446` n `27`; metal avg `0.0543` n `20`; unknown avg `375.945` n `1259`
- 4h: commodity avg `0.0147` n `13`; crypto_alt avg `1.4928` n `239`; crypto_major avg `1.1669` n `8`; equity avg `1.5681` n `168`; fx avg `-0.0612` n `6`; index avg `0.1286` n `27`; metal avg `0.1465` n `20`; unknown avg `66.41` n `1199`
- 24h: commodity avg `0.6015` n `13`; crypto_alt avg `4.5381` n `239`; crypto_major avg `3.4975` n `8`; equity avg `2.341` n `168`; fx avg `-0.0447` n `6`; index avg `0.2269` n `27`; metal avg `0.3057` n `20`; unknown avg `770.5799` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1947`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
