# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T13:37:36.671834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.7108` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.5489` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.5307` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.0777` n `228`; crypto_major avg `-0.2424` n `8`; equity avg `0.4515` n `74`; fx avg `0.0087` n `6`; index avg `0.1152` n `23`; metal avg `-0.0108` n `18`; unknown avg `0.4866` n `689`
- 1h: commodity avg `0.0849` n `12`; crypto_alt avg `0.9313` n `228`; crypto_major avg `0.9126` n `8`; equity avg `0.6375` n `74`; fx avg `0.0211` n `6`; index avg `0.2483` n `23`; metal avg `0.3057` n `18`; unknown avg `0.0131` n `689`
- 4h: commodity avg `0.3897` n `12`; crypto_alt avg `2.5741` n `228`; crypto_major avg `3.1005` n `8`; equity avg `0.5516` n `74`; fx avg `0.0061` n `6`; index avg `0.3218` n `23`; metal avg `0.5698` n `18`; unknown avg `0.7548` n `689`
- 24h: commodity avg `-1.0941` n `12`; crypto_alt avg `6.1928` n `228`; crypto_major avg `6.2525` n `8`; equity avg `2.2301` n `74`; fx avg `0.0496` n `6`; index avg `1.155` n `23`; metal avg `3.0432` n `18`; unknown avg `1.8659` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
