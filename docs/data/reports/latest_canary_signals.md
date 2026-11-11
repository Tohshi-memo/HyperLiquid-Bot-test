# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T21:37:29.629431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `-0.2623` n `239`; crypto_major avg `-0.1804` n `8`; equity avg `0.0715` n `161`; fx avg `0.0035` n `6`; index avg `0.013` n `27`; metal avg `-0.0116` n `20`; unknown avg `0.8771` n `1264`
- 1h: commodity avg `0.0684` n `13`; crypto_alt avg `-0.2281` n `239`; crypto_major avg `0.0458` n `8`; equity avg `-0.0603` n `161`; fx avg `-0.0096` n `6`; index avg `-0.0276` n `27`; metal avg `-0.0524` n `20`; unknown avg `2.2942` n `1218`
- 4h: commodity avg `-0.1631` n `13`; crypto_alt avg `-0.9924` n `239`; crypto_major avg `-0.4914` n `8`; equity avg `-1.0521` n `161`; fx avg `0.0197` n `6`; index avg `-0.0842` n `27`; metal avg `-0.207` n `20`; unknown avg `2.973` n `1210`
- 24h: commodity avg `0.1975` n `13`; crypto_alt avg `0.3428` n `239`; crypto_major avg `0.8016` n `8`; equity avg `4.576` n `161`; fx avg `-0.1499` n `6`; index avg `0.4498` n `27`; metal avg `-0.063` n `20`; unknown avg `3.9694` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
