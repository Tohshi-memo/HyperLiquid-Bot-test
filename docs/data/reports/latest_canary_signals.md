# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T10:37:14.144600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.7979` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.7738` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0413` n `12`; crypto_alt avg `-0.0664` n `228`; crypto_major avg `0.1009` n `8`; equity avg `0.0322` n `65`; fx avg `0.0` n `5`; index avg `0.0227` n `23`; metal avg `0.0155` n `18`; unknown avg `0.0503` n `383`
- 1h: commodity avg `-0.0423` n `12`; crypto_alt avg `0.3411` n `228`; crypto_major avg `0.5868` n `8`; equity avg `0.1517` n `65`; fx avg `-0.0004` n `5`; index avg `0.0907` n `23`; metal avg `0.0254` n `18`; unknown avg `0.1757` n `383`
- 4h: commodity avg `1.7411` n `12`; crypto_alt avg `-8.662` n `228`; crypto_major avg `-2.0327` n `8`; equity avg `-2.6358` n `65`; fx avg `-0.1689` n `5`; index avg `-1.6694` n `23`; metal avg `-5.8306` n `18`; unknown avg `550.2234` n `367`
- 24h: commodity avg `1.7411` n `12`; crypto_alt avg `-8.662` n `228`; crypto_major avg `-2.0327` n `8`; equity avg `-2.6358` n `65`; fx avg `-0.1689` n `5`; index avg `-1.6694` n `23`; metal avg `-5.8306` n `18`; unknown avg `550.2234` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
