# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T17:22:19.676227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1545` n `12`; crypto_alt avg `-0.035` n `228`; crypto_major avg `-0.1497` n `8`; equity avg `-0.015` n `67`; fx avg `0.0089` n `6`; index avg `0.3367` n `23`; metal avg `0.0396` n `18`; unknown avg `0.5544` n `405`
- 1h: commodity avg `-0.4256` n `12`; crypto_alt avg `0.4042` n `228`; crypto_major avg `-0.0305` n `8`; equity avg `0.0769` n `67`; fx avg `-0.0042` n `6`; index avg `0.2816` n `23`; metal avg `0.234` n `18`; unknown avg `0.4928` n `405`
- 4h: commodity avg `-0.8683` n `12`; crypto_alt avg `1.0502` n `228`; crypto_major avg `-0.0631` n `8`; equity avg `0.1571` n `67`; fx avg `-0.0321` n `6`; index avg `0.3719` n `23`; metal avg `0.8084` n `18`; unknown avg `1.5079` n `405`
- 24h: commodity avg `-1.1954` n `12`; crypto_alt avg `2.3341` n `228`; crypto_major avg `0.5529` n `8`; equity avg `0.9075` n `67`; fx avg `-0.0318` n `6`; index avg `0.8176` n `23`; metal avg `1.7329` n `18`; unknown avg `2.326` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
