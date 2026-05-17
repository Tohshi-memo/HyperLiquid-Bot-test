# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T11:07:13.291464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9482` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6852` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.2078` n `228`; crypto_major avg `-0.0505` n `8`; equity avg `0.0081` n `65`; fx avg `0.0006` n `5`; index avg `0.0063` n `23`; metal avg `-0.0277` n `18`; unknown avg `-0.0218` n `383`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.3011` n `228`; crypto_major avg `0.0626` n `8`; equity avg `0.0988` n `65`; fx avg `0.008` n `5`; index avg `0.0775` n `23`; metal avg `-0.0094` n `18`; unknown avg `0.0613` n `383`
- 4h: commodity avg `1.779` n `12`; crypto_alt avg `-8.8778` n `228`; crypto_major avg `-2.1692` n `8`; equity avg `-2.6228` n `65`; fx avg `-0.1676` n `5`; index avg `-1.6596` n `23`; metal avg `-5.8544` n `18`; unknown avg `550.1785` n `367`
- 24h: commodity avg `1.779` n `12`; crypto_alt avg `-8.8778` n `228`; crypto_major avg `-2.1692` n `8`; equity avg `-2.6228` n `65`; fx avg `-0.1676` n `5`; index avg `-1.6596` n `23`; metal avg `-5.8544` n `18`; unknown avg `550.1785` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
