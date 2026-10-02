# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T09:52:28.212173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `0.1089` n `234`; crypto_major avg `0.117` n `8`; equity avg `0.0277` n `142`; fx avg `-0.0121` n `6`; index avg `0.0069` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.3195` n `985`
- 1h: commodity avg `-0.0084` n `13`; crypto_alt avg `-0.0421` n `234`; crypto_major avg `-0.0564` n `8`; equity avg `0.0247` n `142`; fx avg `0.007` n `6`; index avg `0.0056` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.4534` n `983`
- 4h: commodity avg `-0.6676` n `13`; crypto_alt avg `0.651` n `234`; crypto_major avg `0.5628` n `8`; equity avg `0.5825` n `142`; fx avg `-0.0968` n `6`; index avg `0.1377` n `26`; metal avg `-0.0192` n `20`; unknown avg `-0.2061` n `891`
- 24h: commodity avg `-0.6777` n `13`; crypto_alt avg `1.7301` n `234`; crypto_major avg `2.1398` n `8`; equity avg `1.2402` n `142`; fx avg `-0.3435` n `6`; index avg `0.2392` n `26`; metal avg `0.213` n `20`; unknown avg `0.0462` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
