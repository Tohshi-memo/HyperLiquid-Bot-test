# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T23:07:28.686908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `0.0566` n `8`; equity avg `-0.0527` n `100`; fx avg `0.0545` n `6`; index avg `-0.005` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0171` n `774`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.2595` n `230`; crypto_major avg `0.2226` n `8`; equity avg `-0.0352` n `100`; fx avg `0.0514` n `6`; index avg `0.0` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0089` n `774`
- 4h: commodity avg `0.19` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `-0.0673` n `8`; equity avg `0.0731` n `100`; fx avg `0.0413` n `6`; index avg `-0.0038` n `25`; metal avg `0.0177` n `20`; unknown avg `0.0171` n `773`
- 24h: commodity avg `-0.2911` n `12`; crypto_alt avg `-0.9469` n `230`; crypto_major avg `-1.0882` n `8`; equity avg `-3.2499` n `100`; fx avg `-0.1174` n `6`; index avg `-0.471` n `25`; metal avg `0.0172` n `20`; unknown avg `14.0259` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1264`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.122`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
