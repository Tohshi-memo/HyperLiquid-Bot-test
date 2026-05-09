# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T00:37:14.324372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `12`; crypto_alt avg `0.2149` n `228`; crypto_major avg `0.1087` n `8`; equity avg `0.0669` n `65`; fx avg `0.0008` n `5`; index avg `0.0744` n `23`; metal avg `0.0047` n `18`; unknown avg `-0.0001` n `375`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.656` n `228`; crypto_major avg `0.4263` n `8`; equity avg `0.0834` n `65`; fx avg `-0.007` n `5`; index avg `0.0049` n `23`; metal avg `0.0097` n `18`; unknown avg `-0.2033` n `375`
- 4h: commodity avg `-0.1538` n `12`; crypto_alt avg `0.9597` n `228`; crypto_major avg `0.3092` n `8`; equity avg `0.243` n `65`; fx avg `-0.0343` n `5`; index avg `0.1233` n `23`; metal avg `-0.235` n `18`; unknown avg `-0.2328` n `375`
- 24h: commodity avg `-0.8774` n `12`; crypto_alt avg `3.8932` n `228`; crypto_major avg `1.7829` n `8`; equity avg `3.7906` n `65`; fx avg `0.1227` n `5`; index avg `1.4591` n `23`; metal avg `0.6478` n `18`; unknown avg `1.0034` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
