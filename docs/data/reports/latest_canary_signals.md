# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T08:37:28.479099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1075` n `13`; crypto_alt avg `0.1408` n `238`; crypto_major avg `0.1997` n `8`; equity avg `0.0796` n `156`; fx avg `-0.0006` n `6`; index avg `0.007` n `27`; metal avg `0.0051` n `20`; unknown avg `0.1679` n `1260`
- 1h: commodity avg `-0.1771` n `13`; crypto_alt avg `0.1804` n `238`; crypto_major avg `0.4009` n `8`; equity avg `0.0346` n `156`; fx avg `0.0036` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0261` n `20`; unknown avg `7.7658` n `1170`
- 4h: commodity avg `-0.1981` n `13`; crypto_alt avg `-1.0658` n `238`; crypto_major avg `-0.6408` n `8`; equity avg `-0.3893` n `156`; fx avg `0.0261` n `6`; index avg `-0.0695` n `27`; metal avg `0.0538` n `20`; unknown avg `3.2254` n `1151`
- 24h: commodity avg `-0.5981` n `13`; crypto_alt avg `-1.8863` n `238`; crypto_major avg `-0.2439` n `8`; equity avg `0.9024` n `156`; fx avg `0.2436` n `6`; index avg `0.2759` n `27`; metal avg `0.0904` n `20`; unknown avg `2.4933` n `1063`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
