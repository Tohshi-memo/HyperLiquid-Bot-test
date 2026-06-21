# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T07:22:25.389199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.0576` n `228`; crypto_major avg `0.0305` n `8`; equity avg `0.0234` n `78`; fx avg `-0.0044` n `6`; index avg `0.0096` n `23`; metal avg `0.0039` n `18`; unknown avg `0.4223` n `702`
- 1h: commodity avg `-0.063` n `12`; crypto_alt avg `0.1137` n `228`; crypto_major avg `0.113` n `8`; equity avg `0.1137` n `78`; fx avg `-0.003` n `6`; index avg `0.0213` n `23`; metal avg `0.0464` n `18`; unknown avg `0.4807` n `702`
- 4h: commodity avg `-0.0741` n `12`; crypto_alt avg `-0.1104` n `228`; crypto_major avg `-0.4657` n `8`; equity avg `0.2243` n `78`; fx avg `-0.0039` n `6`; index avg `0.0265` n `23`; metal avg `0.0638` n `18`; unknown avg `0.2375` n `662`
- 24h: commodity avg `-0.0075` n `12`; crypto_alt avg `1.0635` n `228`; crypto_major avg `0.14` n `8`; equity avg `0.3396` n `78`; fx avg `0.0522` n `6`; index avg `0.0637` n `23`; metal avg `0.0014` n `18`; unknown avg `-0.1253` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
