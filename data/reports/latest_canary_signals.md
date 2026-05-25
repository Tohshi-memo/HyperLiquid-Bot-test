# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T19:07:19.861134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3572` n `12`; crypto_alt avg `-0.1688` n `228`; crypto_major avg `-0.0826` n `8`; equity avg `-0.0547` n `67`; fx avg `0.0` n `6`; index avg `-0.0198` n `23`; metal avg `-0.002` n `18`; unknown avg `0.4066` n `405`
- 1h: commodity avg `-0.0612` n `12`; crypto_alt avg `-0.2985` n `228`; crypto_major avg `-0.2643` n `8`; equity avg `-0.0351` n `67`; fx avg `0.0087` n `6`; index avg `-0.0943` n `23`; metal avg `0.0258` n `18`; unknown avg `0.0671` n `405`
- 4h: commodity avg `-0.5683` n `12`; crypto_alt avg `-0.0686` n `228`; crypto_major avg `-0.63` n `8`; equity avg `-0.0463` n `67`; fx avg `0.0012` n `6`; index avg `0.1431` n `23`; metal avg `0.1032` n `18`; unknown avg `-0.1708` n `405`
- 24h: commodity avg `-1.1887` n `12`; crypto_alt avg `2.0633` n `228`; crypto_major avg `0.2807` n `8`; equity avg `0.871` n `67`; fx avg `-0.0197` n `6`; index avg `0.5302` n `23`; metal avg `1.5833` n `18`; unknown avg `1.2693` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
