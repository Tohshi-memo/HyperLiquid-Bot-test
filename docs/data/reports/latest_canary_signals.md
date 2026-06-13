# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T01:22:31.939899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `0.0875` n `228`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0163` n `74`; fx avg `0.0227` n `6`; index avg `0.0159` n `23`; metal avg `-0.0011` n `18`; unknown avg `-0.0054` n `643`
- 1h: commodity avg `0.0812` n `12`; crypto_alt avg `0.4004` n `228`; crypto_major avg `0.114` n `8`; equity avg `-0.1232` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0956` n `23`; metal avg `0.0413` n `18`; unknown avg `0.0692` n `643`
- 4h: commodity avg `-0.1563` n `12`; crypto_alt avg `0.3545` n `228`; crypto_major avg `-0.4478` n `8`; equity avg `0.1389` n `74`; fx avg `0.0552` n `6`; index avg `0.1311` n `23`; metal avg `0.09` n `18`; unknown avg `-0.0034` n `643`
- 24h: commodity avg `-0.7068` n `12`; crypto_alt avg `0.5212` n `228`; crypto_major avg `0.2898` n `8`; equity avg `-0.6008` n `74`; fx avg `0.0478` n `6`; index avg `0.4811` n `23`; metal avg `0.826` n `18`; unknown avg `40.7559` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
