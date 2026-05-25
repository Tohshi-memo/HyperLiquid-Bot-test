# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T18:14:55.811229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0646` n `12`; crypto_alt avg `0.0997` n `228`; crypto_major avg `0.0615` n `8`; equity avg `-0.0097` n `67`; fx avg `0.003` n `6`; index avg `0.0869` n `23`; metal avg `0.0137` n `18`; unknown avg `0.2749` n `405`
- 1h: commodity avg `0.327` n `12`; crypto_alt avg `-0.0089` n `228`; crypto_major avg `-0.087` n `8`; equity avg `0.017` n `67`; fx avg `0.0075` n `6`; index avg `0.2252` n `23`; metal avg `-0.1153` n `18`; unknown avg `0.044` n `405`
- 4h: commodity avg `-0.4903` n `12`; crypto_alt avg `0.7009` n `228`; crypto_major avg `-0.2175` n `8`; equity avg `0.0618` n `67`; fx avg `-0.0182` n `6`; index avg `0.1939` n `23`; metal avg `0.3526` n `18`; unknown avg `-0.2266` n `405`
- 24h: commodity avg `-1.1003` n `12`; crypto_alt avg `2.2957` n `228`; crypto_major avg `0.6655` n `8`; equity avg `0.8824` n `67`; fx avg `-0.0228` n `6`; index avg `0.6175` n `23`; metal avg `1.5308` n `18`; unknown avg `1.2125` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
