# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T16:07:32.439707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0214` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.7318` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9595` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `0.0317` n `228`; crypto_major avg `0.1077` n `8`; equity avg `0.1827` n `88`; fx avg `0.0002` n `6`; index avg `0.0139` n `25`; metal avg `0.0558` n `20`; unknown avg `0.2525` n `763`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `0.1229` n `228`; crypto_major avg `0.3378` n `8`; equity avg `0.3428` n `88`; fx avg `-0.0146` n `6`; index avg `0.0164` n `25`; metal avg `0.0518` n `20`; unknown avg `0.2169` n `763`
- 4h: commodity avg `-0.2556` n `12`; crypto_alt avg `2.0092` n `228`; crypto_major avg `2.7658` n `8`; equity avg `0.034` n `88`; fx avg `-0.0597` n `6`; index avg `-0.149` n `25`; metal avg `0.8063` n `20`; unknown avg `1.5921` n `763`
- 24h: commodity avg `-0.7185` n `12`; crypto_alt avg `2.1367` n `228`; crypto_major avg `2.2284` n `8`; equity avg `-0.0325` n `88`; fx avg `-0.0221` n `6`; index avg `-0.3503` n `25`; metal avg `0.4319` n `20`; unknown avg `0.6868` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
