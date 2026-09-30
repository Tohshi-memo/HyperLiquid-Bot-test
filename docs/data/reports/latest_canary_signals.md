# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T22:52:30.858548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `0.0036` n `234`; crypto_major avg `-0.0417` n `8`; equity avg `0.0168` n `142`; fx avg `-0.008` n `6`; index avg `0.0128` n `26`; metal avg `-0.0086` n `20`; unknown avg `1.2348` n `975`
- 1h: commodity avg `-0.0627` n `12`; crypto_alt avg `0.7072` n `234`; crypto_major avg `0.2583` n `8`; equity avg `0.2274` n `142`; fx avg `-0.0088` n `6`; index avg `0.0726` n `26`; metal avg `-0.0112` n `20`; unknown avg `0.4512` n `973`
- 4h: commodity avg `-0.1744` n `12`; crypto_alt avg `0.4663` n `234`; crypto_major avg `0.2757` n `8`; equity avg `0.0895` n `142`; fx avg `0.0295` n `6`; index avg `0.0139` n `26`; metal avg `0.0483` n `20`; unknown avg `1.8108` n `887`
- 24h: commodity avg `0.1502` n `12`; crypto_alt avg `0.7452` n `234`; crypto_major avg `0.8992` n `8`; equity avg `-0.3274` n `142`; fx avg `0.0756` n `6`; index avg `-0.0256` n `26`; metal avg `-0.2491` n `20`; unknown avg `759.4266` n `813`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
