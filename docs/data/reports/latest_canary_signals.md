# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T09:52:37.958462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `13`; crypto_alt avg `-0.1938` n `239`; crypto_major avg `-0.3289` n `8`; equity avg `-0.1048` n `166`; fx avg `0.0085` n `6`; index avg `-0.0138` n `27`; metal avg `-0.0345` n `20`; unknown avg `0.0602` n `1266`
- 1h: commodity avg `0.0423` n `13`; crypto_alt avg `-0.2271` n `239`; crypto_major avg `-0.3697` n `8`; equity avg `0.2219` n `166`; fx avg `-0.0348` n `6`; index avg `-0.0008` n `27`; metal avg `0.0297` n `20`; unknown avg `27.0249` n `1250`
- 4h: commodity avg `-0.3839` n `13`; crypto_alt avg `-0.0329` n `239`; crypto_major avg `-0.3076` n `8`; equity avg `0.5807` n `166`; fx avg `-0.0198` n `6`; index avg `0.0016` n `27`; metal avg `-0.059` n `20`; unknown avg `200.8399` n `1088`
- 24h: commodity avg `-0.7074` n `13`; crypto_alt avg `0.9397` n `239`; crypto_major avg `0.976` n `8`; equity avg `2.4191` n `166`; fx avg `0.2161` n `6`; index avg `0.1363` n `27`; metal avg `0.4075` n `20`; unknown avg `0.2174` n `1003`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
