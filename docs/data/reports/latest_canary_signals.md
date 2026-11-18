# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T05:22:27.499796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1271` n `13`; crypto_alt avg `0.5328` n `239`; crypto_major avg `0.5858` n `8`; equity avg `0.638` n `163`; fx avg `0.0121` n `6`; index avg `0.0596` n `27`; metal avg `0.1463` n `20`; unknown avg `2.3512` n `1264`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `0.0617` n `239`; crypto_major avg `0.3835` n `8`; equity avg `0.1006` n `163`; fx avg `0.0034` n `6`; index avg `-0.0052` n `27`; metal avg `0.0716` n `20`; unknown avg `3.6975` n `1260`
- 4h: commodity avg `-0.2079` n `13`; crypto_alt avg `-0.1192` n `239`; crypto_major avg `0.2221` n `8`; equity avg `-0.3674` n `163`; fx avg `-0.0271` n `6`; index avg `-0.0116` n `27`; metal avg `-0.2438` n `20`; unknown avg `6.8588` n `1252`
- 24h: commodity avg `0.217` n `13`; crypto_alt avg `-0.2662` n `239`; crypto_major avg `0.161` n `8`; equity avg `0.1909` n `163`; fx avg `-0.0708` n `6`; index avg `0.0026` n `27`; metal avg `-0.8019` n `20`; unknown avg `260.2526` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
