# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T12:07:21.833824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1325` n `12`; crypto_alt avg `-0.1012` n `228`; crypto_major avg `0.0143` n `8`; equity avg `-0.1668` n `74`; fx avg `-0.0143` n `6`; index avg `-0.0547` n `23`; metal avg `0.0546` n `18`; unknown avg `1.0126` n `424`
- 1h: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.254` n `228`; crypto_major avg `-0.2638` n `8`; equity avg `-0.2603` n `74`; fx avg `0.0201` n `6`; index avg `-0.0787` n `23`; metal avg `0.2982` n `18`; unknown avg `3.7498` n `424`
- 4h: commodity avg `-0.0388` n `12`; crypto_alt avg `-0.4093` n `228`; crypto_major avg `-0.355` n `8`; equity avg `0.2224` n `74`; fx avg `0.0435` n `6`; index avg `0.0632` n `23`; metal avg `0.5788` n `18`; unknown avg `2.4311` n `424`
- 24h: commodity avg `0.0865` n `12`; crypto_alt avg `-4.0344` n `228`; crypto_major avg `-2.6724` n `8`; equity avg `-0.4262` n `73`; fx avg `0.1305` n `6`; index avg `0.0677` n `23`; metal avg `-0.6242` n `18`; unknown avg `0.4871` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
