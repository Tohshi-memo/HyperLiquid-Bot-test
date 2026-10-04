# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T18:52:30.601899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `0.0408` n `235`; crypto_major avg `-0.0318` n `8`; equity avg `-0.0024` n `144`; fx avg `0.0015` n `6`; index avg `0.0027` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0304` n `1078`
- 1h: commodity avg `0.0101` n `13`; crypto_alt avg `0.2742` n `235`; crypto_major avg `-0.0797` n `8`; equity avg `0.0029` n `144`; fx avg `0.0006` n `6`; index avg `0.0063` n `26`; metal avg `0.0083` n `20`; unknown avg `-0.1452` n `1074`
- 4h: commodity avg `0.0773` n `13`; crypto_alt avg `0.0273` n `235`; crypto_major avg `0.2848` n `8`; equity avg `0.0134` n `144`; fx avg `0.0022` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0` n `20`; unknown avg `-0.1435` n `1068`
- 24h: commodity avg `0.0681` n `13`; crypto_alt avg `1.2133` n `235`; crypto_major avg `0.9057` n `8`; equity avg `0.2043` n `144`; fx avg `0.0294` n `6`; index avg `-0.0123` n `26`; metal avg `0.0089` n `20`; unknown avg `-0.1849` n `1017`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
