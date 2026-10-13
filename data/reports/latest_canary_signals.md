# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T12:37:34.032051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `0.7605` n `235`; crypto_major avg `0.4577` n `8`; equity avg `0.0113` n `151`; fx avg `0.0043` n `6`; index avg `0.0022` n `26`; metal avg `0.0182` n `20`; unknown avg `0.4561` n `1135`
- 1h: commodity avg `0.0339` n `13`; crypto_alt avg `0.3489` n `235`; crypto_major avg `-0.0121` n `8`; equity avg `-0.3068` n `151`; fx avg `0.0217` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0844` n `20`; unknown avg `0.369` n `1127`
- 4h: commodity avg `0.1363` n `13`; crypto_alt avg `-1.4578` n `235`; crypto_major avg `-0.9406` n `8`; equity avg `-0.9324` n `151`; fx avg `0.024` n `6`; index avg `-0.084` n `26`; metal avg `-0.1428` n `20`; unknown avg `0.3885` n `1127`
- 24h: commodity avg `-0.0075` n `13`; crypto_alt avg `-3.5596` n `235`; crypto_major avg `-1.5545` n `8`; equity avg `-3.1769` n `151`; fx avg `0.0931` n `6`; index avg `-0.3579` n `26`; metal avg `0.0014` n `20`; unknown avg `0.3873` n `990`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1706`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1694`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1488`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1478`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0892`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
