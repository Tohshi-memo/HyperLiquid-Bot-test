# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T00:07:24.838038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.1897` n `230`; crypto_major avg `-0.1502` n `8`; equity avg `-0.1849` n `100`; fx avg `-0.0252` n `6`; index avg `-0.0514` n `25`; metal avg `-0.0259` n `20`; unknown avg `0.1925` n `772`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `-0.3277` n `230`; crypto_major avg `-0.3978` n `8`; equity avg `-0.2714` n `100`; fx avg `-0.0287` n `6`; index avg `-0.058` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.265` n `772`
- 4h: commodity avg `0.1285` n `12`; crypto_alt avg `-0.5677` n `230`; crypto_major avg `-0.4131` n `8`; equity avg `-0.4349` n `100`; fx avg `-0.0337` n `6`; index avg `-0.0952` n `25`; metal avg `-0.0372` n `20`; unknown avg `-0.2808` n `772`
- 24h: commodity avg `0.6905` n `12`; crypto_alt avg `-1.952` n `230`; crypto_major avg `-2.6453` n `8`; equity avg `-1.7563` n `99`; fx avg `-0.1067` n `6`; index avg `-0.3759` n `25`; metal avg `-0.7961` n `20`; unknown avg `-0.3377` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
