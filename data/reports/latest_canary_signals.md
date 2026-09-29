# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T08:07:28.342314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0543` n `12`; crypto_alt avg `-0.1704` n `234`; crypto_major avg `-0.0827` n `8`; equity avg `0.005` n `141`; fx avg `0.009` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0444` n `20`; unknown avg `0.1293` n `945`
- 1h: commodity avg `-0.0923` n `12`; crypto_alt avg `0.1909` n `234`; crypto_major avg `-0.0169` n `8`; equity avg `0.1304` n `141`; fx avg `-0.0102` n `6`; index avg `0.0123` n `26`; metal avg `-0.0732` n `20`; unknown avg `0.336` n `945`
- 4h: commodity avg `-0.1644` n `12`; crypto_alt avg `2.2971` n `234`; crypto_major avg `1.4218` n `8`; equity avg `0.797` n `141`; fx avg `-0.037` n `6`; index avg `0.1174` n `26`; metal avg `0.0245` n `20`; unknown avg `13.707` n `927`
- 24h: commodity avg `-0.1599` n `12`; crypto_alt avg `1.139` n `234`; crypto_major avg `1.1621` n `8`; equity avg `-0.6035` n `141`; fx avg `-0.0491` n `6`; index avg `-0.0521` n `26`; metal avg `-0.3021` n `20`; unknown avg `37.2246` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
