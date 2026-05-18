# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T22:22:14.494374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6071` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `0.1472` n `228`; crypto_major avg `0.2063` n `8`; equity avg `0.0899` n `66`; fx avg `0.0056` n `6`; index avg `0.0332` n `23`; metal avg `0.1222` n `18`; unknown avg `-0.0055` n `383`
- 1h: commodity avg `-0.0383` n `12`; crypto_alt avg `0.7759` n `228`; crypto_major avg `0.4824` n `8`; equity avg `0.2841` n `66`; fx avg `0.0093` n `6`; index avg `0.1822` n `23`; metal avg `0.1552` n `18`; unknown avg `-0.1356` n `383`
- 4h: commodity avg `-0.6433` n `12`; crypto_alt avg `2.3678` n `228`; crypto_major avg `1.9638` n `8`; equity avg `1.2635` n `66`; fx avg `-0.0022` n `6`; index avg `0.7274` n `23`; metal avg `0.8361` n `18`; unknown avg `1.0073` n `383`
- 24h: commodity avg `0.8978` n `12`; crypto_alt avg `-0.5582` n `228`; crypto_major avg `-1.1052` n `8`; equity avg `-0.6101` n `66`; fx avg `0.1802` n `6`; index avg `-0.197` n `23`; metal avg `0.9363` n `18`; unknown avg `-0.0693` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
