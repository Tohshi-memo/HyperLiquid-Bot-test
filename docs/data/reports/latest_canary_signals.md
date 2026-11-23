# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T03:22:28.087455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0398` n `13`; crypto_alt avg `1.0809` n `239`; crypto_major avg `1.2365` n `8`; equity avg `0.7339` n `166`; fx avg `-0.0088` n `6`; index avg `0.1291` n `27`; metal avg `0.1749` n `20`; unknown avg `0.9178` n `1262`
- 1h: commodity avg `0.0123` n `13`; crypto_alt avg `1.1495` n `239`; crypto_major avg `1.4551` n `8`; equity avg `0.7991` n `166`; fx avg `-0.0053` n `6`; index avg `0.077` n `27`; metal avg `0.2405` n `20`; unknown avg `1.2717` n `1257`
- 4h: commodity avg `0.0719` n `13`; crypto_alt avg `0.6289` n `239`; crypto_major avg `0.7888` n `8`; equity avg `0.5871` n `166`; fx avg `0.0676` n `6`; index avg `0.0952` n `27`; metal avg `-0.0795` n `20`; unknown avg `160.6249` n `1242`
- 24h: commodity avg `-0.361` n `13`; crypto_alt avg `2.1853` n `239`; crypto_major avg `2.9467` n `8`; equity avg `1.9446` n `166`; fx avg `0.1839` n `6`; index avg `0.2355` n `27`; metal avg `0.4265` n `20`; unknown avg `243.7726` n `1025`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
