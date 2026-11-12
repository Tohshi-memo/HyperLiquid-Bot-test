# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T09:52:26.290646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0541` n `13`; crypto_alt avg `0.084` n `239`; crypto_major avg `0.0195` n `8`; equity avg `-0.0671` n `162`; fx avg `-0.0133` n `6`; index avg `-0.0044` n `27`; metal avg `0.028` n `20`; unknown avg `0.3223` n `1261`
- 1h: commodity avg `-0.1839` n `13`; crypto_alt avg `0.0332` n `239`; crypto_major avg `0.0412` n `8`; equity avg `0.4419` n `162`; fx avg `-0.0143` n `6`; index avg `0.0519` n `27`; metal avg `-0.0205` n `20`; unknown avg `0.9904` n `1255`
- 4h: commodity avg `0.1612` n `13`; crypto_alt avg `-0.0032` n `239`; crypto_major avg `0.0535` n `8`; equity avg `0.8516` n `162`; fx avg `0.0591` n `6`; index avg `0.0512` n `27`; metal avg `-0.2117` n `20`; unknown avg `59.4779` n `1207`
- 24h: commodity avg `0.0385` n `13`; crypto_alt avg `-1.3516` n `239`; crypto_major avg `-0.6406` n `8`; equity avg `-0.4142` n `162`; fx avg `-0.0435` n `6`; index avg `-0.0244` n `27`; metal avg `-0.8782` n `20`; unknown avg `18.1798` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
