# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T08:52:29.481604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0629` n `13`; crypto_alt avg `0.2039` n `239`; crypto_major avg `0.2913` n `8`; equity avg `0.2944` n `166`; fx avg `-0.0038` n `6`; index avg `0.0497` n `27`; metal avg `0.0669` n `20`; unknown avg `0.0334` n `1214`
- 1h: commodity avg `-0.1263` n `13`; crypto_alt avg `0.1257` n `239`; crypto_major avg `0.358` n `8`; equity avg `0.4599` n `166`; fx avg `0.0098` n `6`; index avg `0.0616` n `27`; metal avg `-0.0845` n `20`; unknown avg `0.2273` n `1118`
- 4h: commodity avg `-0.3811` n `13`; crypto_alt avg `0.7823` n `239`; crypto_major avg `0.719` n `8`; equity avg `0.9327` n `166`; fx avg `0.0168` n `6`; index avg `0.037` n `27`; metal avg `0.0905` n `20`; unknown avg `-0.1372` n `1100`
- 24h: commodity avg `-0.7148` n `13`; crypto_alt avg `1.8439` n `239`; crypto_major avg `2.5091` n `8`; equity avg `2.4799` n `166`; fx avg `0.2546` n `6`; index avg `0.159` n `27`; metal avg `0.4538` n `20`; unknown avg `0.7599` n `957`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
