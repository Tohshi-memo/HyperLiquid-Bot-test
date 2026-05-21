# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T08:25:11.501652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0993` n `12`; crypto_alt avg `-0.0334` n `228`; crypto_major avg `0.0576` n `8`; equity avg `0.1211` n `66`; fx avg `0.0361` n `6`; index avg `0.1031` n `23`; metal avg `0.3038` n `18`; unknown avg `0.0289` n `386`
- 1h: commodity avg `-0.4412` n `12`; crypto_alt avg `0.5062` n `228`; crypto_major avg `0.7661` n `8`; equity avg `0.5941` n `66`; fx avg `0.0509` n `6`; index avg `0.3039` n `23`; metal avg `0.4089` n `18`; unknown avg `1.3726` n `385`
- 4h: commodity avg `-0.2` n `12`; crypto_alt avg `0.087` n `228`; crypto_major avg `0.5064` n `8`; equity avg `0.0638` n `66`; fx avg `0.0049` n `6`; index avg `0.0712` n `23`; metal avg `-0.1372` n `18`; unknown avg `0.8008` n `374`
- 24h: commodity avg `-2.0822` n `12`; crypto_alt avg `2.7983` n `228`; crypto_major avg `3.7399` n `8`; equity avg `1.8819` n `66`; fx avg `0.0841` n `6`; index avg `1.4461` n `23`; metal avg `0.4244` n `18`; unknown avg `5.7034` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
