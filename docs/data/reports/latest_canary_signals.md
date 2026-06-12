# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T07:07:28.387943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `12`; crypto_alt avg `0.2348` n `228`; crypto_major avg `0.2096` n `8`; equity avg `-0.1128` n `74`; fx avg `0.0158` n `6`; index avg `-0.0443` n `23`; metal avg `-0.0024` n `18`; unknown avg `0.2093` n `557`
- 1h: commodity avg `0.1369` n `12`; crypto_alt avg `-0.4311` n `228`; crypto_major avg `-0.6865` n `8`; equity avg `-0.549` n `74`; fx avg `0.0197` n `6`; index avg `-0.1967` n `23`; metal avg `-0.1238` n `18`; unknown avg `13.0654` n `557`
- 4h: commodity avg `-0.2676` n `12`; crypto_alt avg `-0.9519` n `228`; crypto_major avg `-1.1526` n `8`; equity avg `-1.1189` n `74`; fx avg `0.0069` n `6`; index avg `-0.4041` n `23`; metal avg `-0.4853` n `18`; unknown avg `16.8518` n `535`
- 24h: commodity avg `-1.8601` n `12`; crypto_alt avg `1.1856` n `228`; crypto_major avg `1.2108` n `8`; equity avg `2.2926` n `74`; fx avg `-0.0413` n `6`; index avg `1.3322` n `23`; metal avg `2.4082` n `18`; unknown avg `1.6422` n `532`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
