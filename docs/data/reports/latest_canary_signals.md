# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T00:52:37.836842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `13`; crypto_alt avg `-0.2621` n `239`; crypto_major avg `-0.1782` n `8`; equity avg `-0.3236` n `157`; fx avg `-0.0103` n `6`; index avg `-0.0295` n `27`; metal avg `-0.0553` n `20`; unknown avg `0.1656` n `1264`
- 1h: commodity avg `0.0718` n `13`; crypto_alt avg `-0.0215` n `239`; crypto_major avg `0.2645` n `8`; equity avg `-0.2016` n `157`; fx avg `-0.0488` n `6`; index avg `-0.0413` n `27`; metal avg `0.0687` n `20`; unknown avg `7.274` n `1252`
- 4h: commodity avg `0.1337` n `13`; crypto_alt avg `0.2623` n `239`; crypto_major avg `0.5064` n `8`; equity avg `0.3204` n `157`; fx avg `-0.055` n `6`; index avg `0.0451` n `27`; metal avg `0.1029` n `20`; unknown avg `215.7053` n `1162`
- 24h: commodity avg `-1.3628` n `13`; crypto_alt avg `-2.5944` n `238`; crypto_major avg `-1.3257` n `8`; equity avg `-3.2753` n `157`; fx avg `0.1046` n `6`; index avg `-0.1967` n `27`; metal avg `0.1404` n `20`; unknown avg `12.8452` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
