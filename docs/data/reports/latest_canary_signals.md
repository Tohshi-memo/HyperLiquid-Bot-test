# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T06:07:26.414257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `0.0536` n `239`; crypto_major avg `0.152` n `8`; equity avg `0.3103` n `164`; fx avg `-0.0058` n `6`; index avg `0.0457` n `27`; metal avg `-0.0411` n `20`; unknown avg `4.8736` n `1234`
- 1h: commodity avg `0.0114` n `13`; crypto_alt avg `-0.1878` n `239`; crypto_major avg `0.0405` n `8`; equity avg `0.176` n `164`; fx avg `-0.0158` n `6`; index avg `0.0467` n `27`; metal avg `0.0256` n `20`; unknown avg `41733.7315` n `1234`
- 4h: commodity avg `-0.0638` n `13`; crypto_alt avg `0.5262` n `239`; crypto_major avg `1.2168` n `8`; equity avg `0.5944` n `164`; fx avg `-0.0092` n `6`; index avg `0.1254` n `27`; metal avg `0.0177` n `20`; unknown avg `47996.8454` n `1217`
- 24h: commodity avg `0.1766` n `13`; crypto_alt avg `-0.3378` n `239`; crypto_major avg `-0.9238` n `8`; equity avg `-0.1926` n `164`; fx avg `-0.1092` n `6`; index avg `0.1038` n `27`; metal avg `-0.3868` n `20`; unknown avg `55398.0349` n `1111`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
