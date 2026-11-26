# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T13:52:24.486840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `13`; crypto_alt avg `0.0817` n `239`; crypto_major avg `0.1186` n `8`; equity avg `0.0084` n `168`; fx avg `0.0043` n `6`; index avg `-0.0037` n `27`; metal avg `0.023` n `20`; unknown avg `157.6326` n `1267`
- 1h: commodity avg `-0.0508` n `13`; crypto_alt avg `0.0079` n `239`; crypto_major avg `0.0935` n `8`; equity avg `-0.0271` n `168`; fx avg `0.0044` n `6`; index avg `-0.0075` n `27`; metal avg `-0.0104` n `20`; unknown avg `0.217` n `1261`
- 4h: commodity avg `0.1728` n `13`; crypto_alt avg `0.1769` n `239`; crypto_major avg `0.0007` n `8`; equity avg `0.2789` n `168`; fx avg `0.0061` n `6`; index avg `0.0338` n `27`; metal avg `-0.082` n `20`; unknown avg `2.8327` n `1251`
- 24h: commodity avg `0.2785` n `13`; crypto_alt avg `5.2908` n `239`; crypto_major avg `4.9711` n `8`; equity avg `5.2794` n `168`; fx avg `0.0871` n `6`; index avg `0.5057` n `27`; metal avg `1.0387` n `20`; unknown avg `249.0003` n `1059`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
