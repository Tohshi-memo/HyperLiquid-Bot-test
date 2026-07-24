# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T01:52:26.321846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.0203` n `230`; crypto_major avg `-0.1026` n `8`; equity avg `-0.1508` n `100`; fx avg `-0.0144` n `6`; index avg `-0.0597` n `25`; metal avg `0.0333` n `20`; unknown avg `-0.0674` n `772`
- 1h: commodity avg `-0.091` n `12`; crypto_alt avg `0.4567` n `230`; crypto_major avg `0.2792` n `8`; equity avg `0.0208` n `100`; fx avg `-0.0533` n `6`; index avg `-0.0366` n `25`; metal avg `-0.0432` n `20`; unknown avg `-0.0142` n `772`
- 4h: commodity avg `-0.1204` n `12`; crypto_alt avg `-0.0123` n `230`; crypto_major avg `-0.0769` n `8`; equity avg `-0.412` n `100`; fx avg `-0.1036` n `6`; index avg `-0.1777` n `25`; metal avg `-0.0809` n `20`; unknown avg `-0.4857` n `772`
- 24h: commodity avg `0.4983` n `12`; crypto_alt avg `-1.3832` n `230`; crypto_major avg `-2.0478` n `8`; equity avg `-1.8651` n `99`; fx avg `-0.0857` n `6`; index avg `-0.4971` n `25`; metal avg `-0.8338` n `20`; unknown avg `-0.3641` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0885`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
