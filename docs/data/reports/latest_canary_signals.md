# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T03:22:28.945451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.2618` n `230`; crypto_major avg `0.2454` n `8`; equity avg `0.0321` n `100`; fx avg `0.0003` n `6`; index avg `0.025` n `25`; metal avg `0.0125` n `20`; unknown avg `0.2243` n `772`
- 1h: commodity avg `0.0389` n `12`; crypto_alt avg `0.2047` n `230`; crypto_major avg `0.2504` n `8`; equity avg `-0.2933` n `100`; fx avg `-0.0006` n `6`; index avg `-0.0793` n `25`; metal avg `-0.1124` n `20`; unknown avg `0.3139` n `772`
- 4h: commodity avg `0.0086` n `12`; crypto_alt avg `0.2476` n `230`; crypto_major avg `0.0102` n `8`; equity avg `-0.8614` n `100`; fx avg `-0.1176` n `6`; index avg `-0.2784` n `25`; metal avg `-0.1948` n `20`; unknown avg `-0.4418` n `772`
- 24h: commodity avg `0.4822` n `12`; crypto_alt avg `-0.8006` n `230`; crypto_major avg `-1.5826` n `8`; equity avg `-1.8448` n `99`; fx avg `-0.1235` n `6`; index avg `-0.5089` n `25`; metal avg `-1.0874` n `20`; unknown avg `-0.3272` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1109`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.101`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0893`, n `666`, weak_sample_signal
