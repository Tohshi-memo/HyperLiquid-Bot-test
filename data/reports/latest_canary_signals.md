# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T09:37:12.415603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3994` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.2389` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.093` n `228`; crypto_major avg `-0.0726` n `8`; equity avg `0.0347` n `65`; fx avg `0.0024` n `5`; index avg `-0.0009` n `23`; metal avg `-0.0206` n `18`; unknown avg `0.2388` n `383`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0689` n `228`; crypto_major avg `0.0732` n `8`; equity avg `0.1112` n `65`; fx avg `0.0024` n `5`; index avg `0.0295` n `23`; metal avg `-0.0447` n `18`; unknown avg `0.2037` n `383`
- 4h: commodity avg `1.7856` n `12`; crypto_alt avg `-8.958` n `228`; crypto_major avg `-2.6138` n `8`; equity avg `-2.7818` n `65`; fx avg `-0.1685` n `5`; index avg `-1.7563` n `23`; metal avg `-5.8527` n `18`; unknown avg `550.3682` n `367`
- 24h: commodity avg `1.7856` n `12`; crypto_alt avg `-8.958` n `228`; crypto_major avg `-2.6138` n `8`; equity avg `-2.7818` n `65`; fx avg `-0.1685` n `5`; index avg `-1.7563` n `23`; metal avg `-5.8527` n `18`; unknown avg `550.3682` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
