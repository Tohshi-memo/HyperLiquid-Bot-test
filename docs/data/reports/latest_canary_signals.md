# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T00:07:31.456701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `-0.0529` n `239`; crypto_major avg `-0.108` n `8`; equity avg `0.3035` n `166`; fx avg `-0.0145` n `6`; index avg `0.0705` n `27`; metal avg `-0.0697` n `20`; unknown avg `-0.0065` n `1249`
- 1h: commodity avg `-0.1469` n `13`; crypto_alt avg `0.2423` n `239`; crypto_major avg `0.1632` n `8`; equity avg `0.9265` n `166`; fx avg `-0.0166` n `6`; index avg `0.1942` n `27`; metal avg `0.104` n `20`; unknown avg `160.1305` n `1250`
- 4h: commodity avg `-0.363` n `13`; crypto_alt avg `0.1046` n `239`; crypto_major avg `0.4099` n `8`; equity avg `0.6941` n `166`; fx avg `0.0821` n `6`; index avg `0.1356` n `27`; metal avg `0.2605` n `20`; unknown avg `540.7016` n `1202`
- 24h: commodity avg `-0.4777` n `13`; crypto_alt avg `0.5997` n `239`; crypto_major avg `0.9538` n `8`; equity avg `1.398` n `166`; fx avg `0.0646` n `6`; index avg `0.1913` n `27`; metal avg `0.283` n `20`; unknown avg `194.7221` n `1031`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
