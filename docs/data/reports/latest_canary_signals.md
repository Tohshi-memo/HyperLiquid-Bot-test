# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T19:52:19.677198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.0893` n `228`; crypto_major avg `-0.0189` n `8`; equity avg `0.0246` n `65`; fx avg `-0.0296` n `5`; index avg `-0.0014` n `23`; metal avg `-0.024` n `18`; unknown avg `-0.2161` n `375`
- 1h: commodity avg `-0.0958` n `12`; crypto_alt avg `-0.174` n `228`; crypto_major avg `-0.1328` n `8`; equity avg `0.1483` n `65`; fx avg `0.0016` n `5`; index avg `0.0019` n `23`; metal avg `0.05` n `18`; unknown avg `-0.1268` n `375`
- 4h: commodity avg `-0.5452` n `12`; crypto_alt avg `1.4629` n `228`; crypto_major avg `1.1573` n `8`; equity avg `0.8399` n `65`; fx avg `0.0217` n `5`; index avg `0.339` n `23`; metal avg `0.4588` n `18`; unknown avg `-0.1035` n `375`
- 24h: commodity avg `-0.3384` n `12`; crypto_alt avg `3.0565` n `228`; crypto_major avg `1.4967` n `8`; equity avg `3.3275` n `65`; fx avg `0.1772` n `5`; index avg `1.4583` n `23`; metal avg `0.9287` n `18`; unknown avg `0.6375` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1258`, n `667`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1223`, n `667`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0947`, n `667`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `667`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
