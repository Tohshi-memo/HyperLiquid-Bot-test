# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T06:37:34.833117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.1835` n `238`; crypto_major avg `-0.1541` n `8`; equity avg `-0.0484` n `156`; fx avg `0.0217` n `6`; index avg `0.0019` n `27`; metal avg `-0.0255` n `20`; unknown avg `-0.0942` n `1260`
- 1h: commodity avg `0.106` n `13`; crypto_alt avg `-0.8403` n `238`; crypto_major avg `-0.5078` n `8`; equity avg `-0.2233` n `156`; fx avg `0.0283` n `6`; index avg `-0.0533` n `27`; metal avg `-0.0759` n `20`; unknown avg `0.3819` n `1238`
- 4h: commodity avg `-0.061` n `13`; crypto_alt avg `-0.9928` n `238`; crypto_major avg `-0.4163` n `8`; equity avg `0.3946` n `156`; fx avg `0.0399` n `6`; index avg `0.0848` n `27`; metal avg `0.0717` n `20`; unknown avg `1.355` n `1177`
- 24h: commodity avg `-0.3575` n `13`; crypto_alt avg `-1.7909` n `238`; crypto_major avg `-0.1965` n `8`; equity avg `1.0494` n `156`; fx avg `0.2075` n `6`; index avg `0.3224` n `27`; metal avg `0.1095` n `20`; unknown avg `2.8146` n `1069`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
