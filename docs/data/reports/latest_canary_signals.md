# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T21:37:25.964905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1657` n `12`; crypto_alt avg `-0.0969` n `228`; crypto_major avg `-0.1061` n `8`; equity avg `-0.0592` n `74`; fx avg `-0.0392` n `6`; index avg `-0.0432` n `23`; metal avg `-0.0215` n `18`; unknown avg `-0.126` n `556`
- 1h: commodity avg `-0.0902` n `12`; crypto_alt avg `0.6637` n `228`; crypto_major avg `0.4901` n `8`; equity avg `0.1809` n `74`; fx avg `0.0246` n `6`; index avg `0.0359` n `23`; metal avg `-0.0644` n `18`; unknown avg `-0.0258` n `556`
- 4h: commodity avg `-0.2462` n `12`; crypto_alt avg `0.5955` n `228`; crypto_major avg `0.6344` n `8`; equity avg `1.3916` n `74`; fx avg `-0.0125` n `6`; index avg `0.7672` n `23`; metal avg `1.0154` n `18`; unknown avg `0.2383` n `556`
- 24h: commodity avg `-2.6064` n `12`; crypto_alt avg `4.9168` n `228`; crypto_major avg `4.2853` n `8`; equity avg `4.0667` n `74`; fx avg `0.064` n `6`; index avg `2.3745` n `23`; metal avg `3.4968` n `18`; unknown avg `2.4351` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
