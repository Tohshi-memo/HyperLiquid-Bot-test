# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T16:07:35.739454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0954` n `12`; crypto_alt avg `0.3965` n `228`; crypto_major avg `0.2978` n `8`; equity avg `0.227` n `74`; fx avg `-0.0148` n `6`; index avg `0.1101` n `23`; metal avg `0.0589` n `18`; unknown avg `-0.0397` n `556`
- 1h: commodity avg `0.3453` n `12`; crypto_alt avg `0.4866` n `228`; crypto_major avg `0.2573` n `8`; equity avg `0.4984` n `74`; fx avg `-0.0272` n `6`; index avg `0.2964` n `23`; metal avg `0.1767` n `18`; unknown avg `0.0862` n `556`
- 4h: commodity avg `0.3196` n `12`; crypto_alt avg `0.1212` n `228`; crypto_major avg `-0.2317` n `8`; equity avg `-0.0522` n `74`; fx avg `-0.0957` n `6`; index avg `0.0497` n `23`; metal avg `0.4934` n `18`; unknown avg `0.3917` n `556`
- 24h: commodity avg `-0.7865` n `12`; crypto_alt avg `0.2971` n `228`; crypto_major avg `-0.2127` n `8`; equity avg `-0.15` n `74`; fx avg `-0.0446` n `6`; index avg `0.0571` n `23`; metal avg `-0.5123` n `18`; unknown avg `7.0243` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
