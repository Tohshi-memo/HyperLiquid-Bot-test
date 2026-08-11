# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T01:52:27.834904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `0.091` n `230`; crypto_major avg `0.0928` n `8`; equity avg `0.1002` n `113`; fx avg `0.0145` n `6`; index avg `0.0405` n `25`; metal avg `0.0949` n `20`; unknown avg `-0.0442` n `785`
- 1h: commodity avg `0.0228` n `12`; crypto_alt avg `0.151` n `230`; crypto_major avg `0.2966` n `8`; equity avg `0.2439` n `113`; fx avg `0.012` n `6`; index avg `0.0984` n `25`; metal avg `0.1801` n `20`; unknown avg `-0.1219` n `785`
- 4h: commodity avg `0.015` n `12`; crypto_alt avg `0.3885` n `230`; crypto_major avg `0.0861` n `8`; equity avg `0.3709` n `113`; fx avg `-0.031` n `6`; index avg `0.1128` n `25`; metal avg `0.2513` n `20`; unknown avg `-0.2481` n `785`
- 24h: commodity avg `0.8495` n `12`; crypto_alt avg `-0.6927` n `230`; crypto_major avg `-0.8726` n `8`; equity avg `-1.1861` n `113`; fx avg `0.1004` n `6`; index avg `0.0027` n `25`; metal avg `0.7646` n `20`; unknown avg `103.8252` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
