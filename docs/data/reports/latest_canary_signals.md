# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T15:06:29.402373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.0014` n `230`; crypto_major avg `-0.1294` n `8`; equity avg `0.0006` n `102`; fx avg `-0.0208` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.1419` n `780`
- 1h: commodity avg `0.0668` n `12`; crypto_alt avg `0.6635` n `230`; crypto_major avg `0.1157` n `8`; equity avg `0.6941` n `102`; fx avg `0.0935` n `6`; index avg `0.1459` n `25`; metal avg `0.2399` n `20`; unknown avg `0.2928` n `780`
- 4h: commodity avg `0.1345` n `12`; crypto_alt avg `-0.1939` n `230`; crypto_major avg `-0.8996` n `8`; equity avg `-2.2356` n `102`; fx avg `-0.1051` n `6`; index avg `-0.2948` n `25`; metal avg `-0.0867` n `20`; unknown avg `1.0054` n `780`
- 24h: commodity avg `0.1431` n `12`; crypto_alt avg `-0.7343` n `230`; crypto_major avg `-1.4524` n `8`; equity avg `1.0153` n `102`; fx avg `0.1083` n `6`; index avg `0.3527` n `25`; metal avg `-0.1211` n `20`; unknown avg `1.5514` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
