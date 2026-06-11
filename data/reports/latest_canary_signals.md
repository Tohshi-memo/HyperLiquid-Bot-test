# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T23:23:03.890192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1469` n `12`; crypto_alt avg `0.0609` n `228`; crypto_major avg `0.1392` n `8`; equity avg `0.0056` n `74`; fx avg `-0.0161` n `6`; index avg `0.0512` n `23`; metal avg `-0.1242` n `18`; unknown avg `-0.0805` n `556`
- 1h: commodity avg `0.0762` n `12`; crypto_alt avg `-0.2741` n `228`; crypto_major avg `-0.1542` n `8`; equity avg `0.036` n `74`; fx avg `0.0218` n `6`; index avg `-0.0193` n `23`; metal avg `0.1935` n `18`; unknown avg `-0.0683` n `556`
- 4h: commodity avg `-0.741` n `12`; crypto_alt avg `0.0136` n `228`; crypto_major avg `-0.1595` n `8`; equity avg `0.8` n `74`; fx avg `0.0179` n `6`; index avg `0.6958` n `23`; metal avg `0.4427` n `18`; unknown avg `-0.4` n `556`
- 24h: commodity avg `-2.826` n `12`; crypto_alt avg `4.3634` n `228`; crypto_major avg `4.2726` n `8`; equity avg `5.3073` n `74`; fx avg `0.1399` n `6`; index avg `2.8675` n `23`; metal avg `4.5274` n `18`; unknown avg `2.4733` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
