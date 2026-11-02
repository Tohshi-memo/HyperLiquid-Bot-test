# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T07:22:24.376154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `13`; crypto_alt avg `-0.075` n `238`; crypto_major avg `-0.0575` n `8`; equity avg `-0.0835` n `156`; fx avg `0.0171` n `6`; index avg `-0.0122` n `27`; metal avg `0.0338` n `20`; unknown avg `-0.0` n `1264`
- 1h: commodity avg `-0.0731` n `13`; crypto_alt avg `-0.1905` n `238`; crypto_major avg `-0.3256` n `8`; equity avg `-0.0831` n `156`; fx avg `0.0439` n `6`; index avg `-0.013` n `27`; metal avg `0.023` n `20`; unknown avg `-0.0933` n `1256`
- 4h: commodity avg `-0.0688` n `13`; crypto_alt avg `-1.1303` n `238`; crypto_major avg `-0.7375` n `8`; equity avg `-0.0951` n `156`; fx avg `0.028` n `6`; index avg `0.0197` n `27`; metal avg `0.1369` n `20`; unknown avg `1.669` n `1175`
- 24h: commodity avg `-0.4122` n `13`; crypto_alt avg `-1.7338` n `238`; crypto_major avg `-0.2262` n `8`; equity avg `1.0452` n `156`; fx avg `0.2455` n `6`; index avg `0.2985` n `27`; metal avg `0.169` n `20`; unknown avg `2.6351` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
