# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T14:37:30.582473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0624` n `12`; crypto_alt avg `0.2828` n `228`; crypto_major avg `0.3885` n `8`; equity avg `0.3396` n `74`; fx avg `-0.0302` n `6`; index avg `0.1141` n `23`; metal avg `0.2495` n `18`; unknown avg `0.1297` n `556`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.266` n `228`; crypto_major avg `0.2347` n `8`; equity avg `0.5217` n `74`; fx avg `-0.0674` n `6`; index avg `0.2672` n `23`; metal avg `0.191` n `18`; unknown avg `0.3772` n `556`
- 4h: commodity avg `0.4186` n `12`; crypto_alt avg `0.1588` n `228`; crypto_major avg `0.2142` n `8`; equity avg `-0.1003` n `74`; fx avg `-0.0449` n `6`; index avg `-0.0028` n `23`; metal avg `0.2681` n `18`; unknown avg `0.5529` n `556`
- 24h: commodity avg `-0.508` n `12`; crypto_alt avg `0.8076` n `228`; crypto_major avg `0.6466` n `8`; equity avg `-1.107` n `74`; fx avg `-0.0366` n `6`; index avg `-0.7958` n `23`; metal avg `-0.8849` n `18`; unknown avg `2.6669` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
