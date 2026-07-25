# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T22:07:38.515655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `0.0032` n `230`; crypto_major avg `-0.0324` n `8`; equity avg `0.0281` n `100`; fx avg `-0.0013` n `6`; index avg `0.0013` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0373` n `774`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `0.2077` n `230`; crypto_major avg `0.0577` n `8`; equity avg `0.0171` n `100`; fx avg `-0.0013` n `6`; index avg `0.0047` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0801` n `774`
- 4h: commodity avg `0.0836` n `12`; crypto_alt avg `-0.1241` n `230`; crypto_major avg `-0.3183` n `8`; equity avg `0.0752` n `100`; fx avg `0.0191` n `6`; index avg `0.0083` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0053` n `774`
- 24h: commodity avg `-0.6276` n `12`; crypto_alt avg `0.8528` n `230`; crypto_major avg `1.2829` n `8`; equity avg `0.3505` n `100`; fx avg `0.0019` n `6`; index avg `0.1452` n `25`; metal avg `0.0221` n `20`; unknown avg `-0.2903` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1352`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1225`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1149`, n `666`, weak_sample_signal
