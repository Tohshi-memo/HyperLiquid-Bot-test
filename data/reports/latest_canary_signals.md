# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T13:37:33.446402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4616` n `12`; crypto_alt avg `0.0107` n `228`; crypto_major avg `0.0432` n `8`; equity avg `-0.0588` n `74`; fx avg `0.0232` n `6`; index avg `-0.0533` n `23`; metal avg `0.198` n `18`; unknown avg `-0.0971` n `556`
- 1h: commodity avg `-0.4247` n `12`; crypto_alt avg `0.3958` n `228`; crypto_major avg `0.3065` n `8`; equity avg `0.1806` n `74`; fx avg `0.0264` n `6`; index avg `0.0888` n `23`; metal avg `0.614` n `18`; unknown avg `-0.1278` n `556`
- 4h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.1401` n `228`; crypto_major avg `-0.0408` n `8`; equity avg `-0.4379` n `74`; fx avg `-0.0043` n `6`; index avg `-0.214` n `23`; metal avg `0.1404` n `18`; unknown avg `-1.6725` n `556`
- 24h: commodity avg `-0.1338` n `12`; crypto_alt avg `-0.0485` n `228`; crypto_major avg `-0.0978` n `8`; equity avg `-1.006` n `74`; fx avg `-0.0134` n `6`; index avg `-0.5714` n `23`; metal avg `-1.113` n `18`; unknown avg `4.0175` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
