# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T19:52:26.695501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `13`; crypto_alt avg `0.2337` n `236`; crypto_major avg `0.2325` n `8`; equity avg `0.0463` n `151`; fx avg `0.0061` n `6`; index avg `0.0148` n `26`; metal avg `-0.0117` n `20`; unknown avg `112.0697` n `1177`
- 1h: commodity avg `-0.0491` n `13`; crypto_alt avg `0.4538` n `236`; crypto_major avg `0.4009` n `8`; equity avg `-0.1197` n `151`; fx avg `0.0037` n `6`; index avg `-0.0037` n `26`; metal avg `0.0718` n `20`; unknown avg `113.6424` n `1175`
- 4h: commodity avg `0.5577` n `13`; crypto_alt avg `-0.9198` n `236`; crypto_major avg `-0.3425` n `8`; equity avg `-1.5281` n `151`; fx avg `0.0002` n `6`; index avg `-0.3101` n `26`; metal avg `-0.0906` n `20`; unknown avg `11.3015` n `1164`
- 24h: commodity avg `0.3075` n `13`; crypto_alt avg `-2.1385` n `236`; crypto_major avg `-1.9327` n `8`; equity avg `-3.9816` n `151`; fx avg `0.011` n `6`; index avg `-0.6602` n `26`; metal avg `-0.1278` n `20`; unknown avg `4.6932` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1597`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1095`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0718`, n `666`, weak_sample_signal
