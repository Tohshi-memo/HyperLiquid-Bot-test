# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T22:37:27.924900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.2011` n `239`; crypto_major avg `-0.105` n `8`; equity avg `-0.0963` n `168`; fx avg `-0.0052` n `6`; index avg `-0.0103` n `27`; metal avg `-0.0092` n `20`; unknown avg `1.8998` n `1261`
- 1h: commodity avg `-0.0178` n `13`; crypto_alt avg `-0.4187` n `239`; crypto_major avg `-0.6991` n `8`; equity avg `-0.2335` n `168`; fx avg `0.0068` n `6`; index avg `-0.0185` n `27`; metal avg `-0.0354` n `20`; unknown avg `2.7058` n `1243`
- 4h: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.035` n `239`; crypto_major avg `0.0768` n `8`; equity avg `0.2383` n `168`; fx avg `-0.0018` n `6`; index avg `0.0189` n `27`; metal avg `0.0174` n `20`; unknown avg `8.7364` n `1177`
- 24h: commodity avg `0.0697` n `13`; crypto_alt avg `1.4727` n `239`; crypto_major avg `0.7301` n `8`; equity avg `1.0538` n `168`; fx avg `-0.0085` n `6`; index avg `0.0894` n `27`; metal avg `-0.0015` n `20`; unknown avg `15.3174` n `1013`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
