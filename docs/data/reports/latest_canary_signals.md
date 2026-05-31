# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T00:52:15.282445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.035` n `12`; crypto_alt avg `0.1243` n `228`; crypto_major avg `-0.0144` n `8`; equity avg `0.0296` n `69`; fx avg `-0.0156` n `6`; index avg `-0.0006` n `23`; metal avg `-0.0128` n `18`; unknown avg `0.3165` n `421`
- 1h: commodity avg `0.0494` n `12`; crypto_alt avg `0.3959` n `228`; crypto_major avg `0.2516` n `8`; equity avg `0.0538` n `69`; fx avg `0.0064` n `6`; index avg `-0.0411` n `23`; metal avg `-0.008` n `18`; unknown avg `-0.059` n `421`
- 4h: commodity avg `0.1283` n `12`; crypto_alt avg `-0.4423` n `228`; crypto_major avg `0.1373` n `8`; equity avg `0.1733` n `69`; fx avg `-0.0246` n `6`; index avg `0.0074` n `23`; metal avg `-0.0316` n `18`; unknown avg `-0.4356` n `421`
- 24h: commodity avg `-0.25` n `12`; crypto_alt avg `0.7863` n `228`; crypto_major avg `2.4875` n `8`; equity avg `1.0196` n `69`; fx avg `0.012` n `6`; index avg `0.0048` n `23`; metal avg `-0.0078` n `18`; unknown avg `0.1497` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
