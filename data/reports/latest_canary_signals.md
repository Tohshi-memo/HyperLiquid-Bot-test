# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T06:07:29.289024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0495` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9996` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0719` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0489` n `13`; crypto_alt avg `-0.17` n `238`; crypto_major avg `0.0064` n `8`; equity avg `-0.096` n `156`; fx avg `0.011` n `6`; index avg `-0.0059` n `27`; metal avg `-0.1013` n `20`; unknown avg `0.4762` n `1238`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `-0.0247` n `238`; crypto_major avg `-0.0086` n `8`; equity avg `-0.5347` n `156`; fx avg `-0.0005` n `6`; index avg `-0.0707` n `27`; metal avg `-0.1457` n `20`; unknown avg `150.8783` n `1238`
- 4h: commodity avg `-0.2333` n `13`; crypto_alt avg `2.9806` n `238`; crypto_major avg `2.8162` n `8`; equity avg `0.7443` n `156`; fx avg `-0.0265` n `6`; index avg `0.08` n `27`; metal avg `-0.1834` n `20`; unknown avg `1.7591` n `1216`
- 24h: commodity avg `-0.0557` n `13`; crypto_alt avg `-3.8951` n `238`; crypto_major avg `-0.1908` n `8`; equity avg `-3.1951` n `155`; fx avg `0.1292` n `6`; index avg `-0.4324` n `27`; metal avg `-0.625` n `20`; unknown avg `29.6124` n `980`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
