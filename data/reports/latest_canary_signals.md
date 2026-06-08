# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T07:22:27.621656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0876` n `12`; crypto_alt avg `0.4214` n `228`; crypto_major avg `0.4163` n `8`; equity avg `0.4198` n `74`; fx avg `0.0279` n `6`; index avg `0.1393` n `23`; metal avg `0.3206` n `18`; unknown avg `0.0138` n `517`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.1364` n `228`; crypto_major avg `0.2288` n `8`; equity avg `0.5831` n `74`; fx avg `-0.0439` n `6`; index avg `0.1749` n `23`; metal avg `0.0349` n `18`; unknown avg `-0.1811` n `517`
- 4h: commodity avg `0.1989` n `12`; crypto_alt avg `-0.2205` n `228`; crypto_major avg `-0.4035` n `8`; equity avg `-0.4666` n `74`; fx avg `-0.2048` n `6`; index avg `-0.2152` n `23`; metal avg `-0.0922` n `18`; unknown avg `-0.2895` n `507`
- 24h: commodity avg `0.8792` n `12`; crypto_alt avg `0.3368` n `228`; crypto_major avg `2.1599` n `8`; equity avg `0.6487` n `74`; fx avg `-0.2914` n `6`; index avg `0.0971` n `23`; metal avg `-0.5784` n `18`; unknown avg `-5.4702` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
