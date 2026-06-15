# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T06:07:39.774251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.78` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0959` n `12`; crypto_alt avg `0.2175` n `228`; crypto_major avg `0.1782` n `8`; equity avg `0.1023` n `74`; fx avg `0.007` n `6`; index avg `0.0833` n `23`; metal avg `-0.0646` n `18`; unknown avg `-0.1325` n `657`
- 1h: commodity avg `0.1713` n `12`; crypto_alt avg `0.5566` n `228`; crypto_major avg `0.2908` n `8`; equity avg `-0.0214` n `74`; fx avg `-0.0195` n `6`; index avg `0.0629` n `23`; metal avg `-0.3983` n `18`; unknown avg `-0.0443` n `529`
- 4h: commodity avg `0.1625` n `12`; crypto_alt avg `0.8391` n `228`; crypto_major avg `0.3992` n `8`; equity avg `0.2659` n `74`; fx avg `-0.0085` n `6`; index avg `0.1595` n `23`; metal avg `-0.4896` n `18`; unknown avg `0.1283` n `529`
- 24h: commodity avg `-0.7449` n `12`; crypto_alt avg `2.7816` n `228`; crypto_major avg `2.7738` n `8`; equity avg `1.8176` n `74`; fx avg `0.0187` n `6`; index avg `0.9662` n `23`; metal avg `1.6114` n `18`; unknown avg `3.8111` n `529`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
