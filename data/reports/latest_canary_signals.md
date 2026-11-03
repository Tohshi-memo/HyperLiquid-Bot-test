# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T01:37:30.224121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.1839` n `239`; crypto_major avg `-0.1549` n `8`; equity avg `-0.083` n `157`; fx avg `0.0001` n `6`; index avg `-0.0257` n `27`; metal avg `-0.083` n `20`; unknown avg `17.46` n `1264`
- 1h: commodity avg `0.0791` n `13`; crypto_alt avg `-0.3968` n `239`; crypto_major avg `-0.1944` n `8`; equity avg `0.0013` n `157`; fx avg `-0.0073` n `6`; index avg `0.0248` n `27`; metal avg `-0.1694` n `20`; unknown avg `0.4662` n `1258`
- 4h: commodity avg `0.0673` n `13`; crypto_alt avg `-0.1829` n `239`; crypto_major avg `0.1831` n `8`; equity avg `0.2744` n `157`; fx avg `-0.0517` n `6`; index avg `0.0501` n `27`; metal avg `-0.0253` n `20`; unknown avg `15.9711` n `1246`
- 24h: commodity avg `-1.1816` n `13`; crypto_alt avg `-3.1018` n `238`; crypto_major avg `-1.986` n `8`; equity avg `-3.2968` n `157`; fx avg `0.1145` n `6`; index avg `-0.1623` n `27`; metal avg `0.0719` n `20`; unknown avg `12.4124` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
