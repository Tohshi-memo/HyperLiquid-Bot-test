# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T06:07:34.892987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.0153` n `228`; crypto_major avg `-0.0221` n `8`; equity avg `0.0129` n `86`; fx avg `-0.0027` n `6`; index avg `-0.0101` n `23`; metal avg `-0.0545` n `20`; unknown avg `-0.1056` n `749`
- 1h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.0696` n `228`; crypto_major avg `-0.0347` n `8`; equity avg `0.0574` n `86`; fx avg `-0.0383` n `6`; index avg `0.0296` n `23`; metal avg `-0.165` n `20`; unknown avg `1.2211` n `749`
- 4h: commodity avg `0.0187` n `12`; crypto_alt avg `0.9864` n `228`; crypto_major avg `1.0148` n `8`; equity avg `0.3517` n `86`; fx avg `-0.0515` n `6`; index avg `0.0821` n `23`; metal avg `0.1653` n `20`; unknown avg `0.0493` n `732`
- 24h: commodity avg `-0.6141` n `12`; crypto_alt avg `-1.0875` n `228`; crypto_major avg `-0.9578` n `8`; equity avg `-0.0511` n `86`; fx avg `-0.0071` n `6`; index avg `0.563` n `23`; metal avg `-1.8949` n `20`; unknown avg `-0.5548` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
