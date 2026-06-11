# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T13:07:36.238154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2278` n `12`; crypto_alt avg `-0.0249` n `228`; crypto_major avg `-0.0548` n `8`; equity avg `-0.0788` n `74`; fx avg `-0.0103` n `6`; index avg `-0.0023` n `23`; metal avg `0.069` n `18`; unknown avg `0.013` n `556`
- 1h: commodity avg `0.7071` n `12`; crypto_alt avg `-0.4675` n `228`; crypto_major avg `-0.4309` n `8`; equity avg `-0.5819` n `74`; fx avg `0.0004` n `6`; index avg `-0.2201` n `23`; metal avg `-0.079` n `18`; unknown avg `0.1676` n `556`
- 4h: commodity avg `0.6457` n `12`; crypto_alt avg `-0.2476` n `228`; crypto_major avg `-0.0897` n `8`; equity avg `-0.4764` n `74`; fx avg `-0.0161` n `6`; index avg `-0.191` n `23`; metal avg `-0.1956` n `18`; unknown avg `-1.1793` n `556`
- 24h: commodity avg `0.0928` n `12`; crypto_alt avg `0.8716` n `228`; crypto_major avg `1.0277` n `8`; equity avg `0.1442` n `74`; fx avg `0.0385` n `6`; index avg `-0.2828` n `23`; metal avg `-1.0346` n `18`; unknown avg `4.447` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
