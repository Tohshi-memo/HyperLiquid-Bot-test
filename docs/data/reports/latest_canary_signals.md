# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T01:22:31.161717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.0526` n `230`; crypto_major avg `0.0294` n `8`; equity avg `0.0173` n `100`; fx avg `-0.0107` n `6`; index avg `0.0025` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.2504` n `772`
- 1h: commodity avg `-0.1532` n `12`; crypto_alt avg `0.1185` n `230`; crypto_major avg `0.1085` n `8`; equity avg `0.0179` n `100`; fx avg `-0.0679` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0542` n `20`; unknown avg `0.0594` n `772`
- 4h: commodity avg `-0.1199` n `12`; crypto_alt avg `-0.2496` n `230`; crypto_major avg `-0.1931` n `8`; equity avg `-0.4576` n `100`; fx avg `-0.0881` n `6`; index avg `-0.1353` n `25`; metal avg `-0.1219` n `20`; unknown avg `-0.5151` n `772`
- 24h: commodity avg `0.4474` n `12`; crypto_alt avg `-1.6692` n `230`; crypto_major avg `-2.2462` n `8`; equity avg `-1.9986` n `99`; fx avg `-0.1048` n `6`; index avg `-0.4895` n `25`; metal avg `-0.9701` n `20`; unknown avg `-0.3825` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
