# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T11:22:27.730452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.0144` n `239`; crypto_major avg `0.0326` n `8`; equity avg `0.0469` n `166`; fx avg `-0.0015` n `6`; index avg `-0.0005` n `27`; metal avg `0.0001` n `20`; unknown avg `-0.1437` n `1260`
- 1h: commodity avg `-0.1241` n `13`; crypto_alt avg `-0.1353` n `239`; crypto_major avg `0.1214` n `8`; equity avg `-0.0224` n `166`; fx avg `-0.0309` n `6`; index avg `0.008` n `27`; metal avg `-0.0153` n `20`; unknown avg `159.1352` n `1256`
- 4h: commodity avg `-0.0138` n `13`; crypto_alt avg `-0.2096` n `239`; crypto_major avg `-0.2244` n `8`; equity avg `-0.2106` n `166`; fx avg `0.0398` n `6`; index avg `-0.0195` n `27`; metal avg `0.0142` n `20`; unknown avg `340.4627` n `1240`
- 24h: commodity avg `0.5342` n `13`; crypto_alt avg `-5.3071` n `239`; crypto_major avg `-5.8818` n `8`; equity avg `-4.2691` n `166`; fx avg `-0.0803` n `6`; index avg `-0.4538` n `27`; metal avg `-0.4638` n `20`; unknown avg `349.018` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
