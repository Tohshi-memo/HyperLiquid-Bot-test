# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T06:52:40.517668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `13`; crypto_alt avg `-0.0192` n `238`; crypto_major avg `-0.0431` n `8`; equity avg `0.0031` n `156`; fx avg `0.0153` n `6`; index avg `0.0026` n `27`; metal avg `0.0187` n `20`; unknown avg `-0.1207` n `1264`
- 1h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.8002` n `238`; crypto_major avg `-0.5741` n `8`; equity avg `-0.2655` n `156`; fx avg `0.0489` n `6`; index avg `-0.0466` n `27`; metal avg `-0.0871` n `20`; unknown avg `0.2539` n `1238`
- 4h: commodity avg `-0.0586` n `13`; crypto_alt avg `-0.9599` n `238`; crypto_major avg `-0.507` n `8`; equity avg `0.4019` n `156`; fx avg `0.0562` n `6`; index avg `0.0983` n `27`; metal avg `0.197` n `20`; unknown avg `1.5476` n `1177`
- 24h: commodity avg `-0.3737` n `13`; crypto_alt avg `-1.82` n `238`; crypto_major avg `-0.3563` n `8`; equity avg `1.0477` n `156`; fx avg `0.2333` n `6`; index avg `0.3158` n `27`; metal avg `0.1274` n `20`; unknown avg `2.6905` n `1069`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
