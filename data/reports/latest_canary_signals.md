# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T19:37:29.548342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2054` n `12`; crypto_alt avg `-0.2208` n `234`; crypto_major avg `-0.3426` n `8`; equity avg `0.1021` n `140`; fx avg `-0.0126` n `6`; index avg `0.0459` n `26`; metal avg `0.1157` n `20`; unknown avg `0.7533` n `942`
- 1h: commodity avg `-0.1869` n `12`; crypto_alt avg `0.1758` n `234`; crypto_major avg `0.1085` n `8`; equity avg `0.1627` n `140`; fx avg `-0.0079` n `6`; index avg `0.0555` n `26`; metal avg `0.1724` n `20`; unknown avg `0.2847` n `940`
- 4h: commodity avg `-0.2023` n `12`; crypto_alt avg `0.8465` n `234`; crypto_major avg `0.3447` n `8`; equity avg `0.5806` n `140`; fx avg `0.0145` n `6`; index avg `0.1406` n `26`; metal avg `0.441` n `20`; unknown avg `0.2081` n `888`
- 24h: commodity avg `0.0081` n `12`; crypto_alt avg `2.3109` n `234`; crypto_major avg `0.9739` n `8`; equity avg `0.7929` n `140`; fx avg `-0.2842` n `6`; index avg `0.1145` n `26`; metal avg `0.3398` n `20`; unknown avg `1.2938` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
