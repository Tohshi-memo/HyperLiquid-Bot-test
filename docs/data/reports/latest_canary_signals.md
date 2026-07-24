# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T04:22:24.339174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.0355` n `230`; crypto_major avg `-0.1135` n `8`; equity avg `-0.0327` n `100`; fx avg `0.0167` n `6`; index avg `-0.0085` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0822` n `772`
- 1h: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.0316` n `230`; crypto_major avg `-0.1104` n `8`; equity avg `-0.1626` n `100`; fx avg `0.0109` n `6`; index avg `-0.0152` n `25`; metal avg `0.0097` n `20`; unknown avg `1.431` n `772`
- 4h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.4766` n `230`; crypto_major avg `0.3163` n `8`; equity avg `-0.6875` n `100`; fx avg `-0.0841` n `6`; index avg `-0.2005` n `25`; metal avg `-0.1615` n `20`; unknown avg `0.5798` n `772`
- 24h: commodity avg `0.5292` n `12`; crypto_alt avg `-1.05` n `230`; crypto_major avg `-1.8045` n `8`; equity avg `-2.2394` n `99`; fx avg `-0.102` n `6`; index avg `-0.6045` n `25`; metal avg `-1.0775` n `20`; unknown avg `-0.2105` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1107`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0995`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0932`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
