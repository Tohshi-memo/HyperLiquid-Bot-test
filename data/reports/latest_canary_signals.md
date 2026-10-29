# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T16:22:33.968941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4374` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2235` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `-0.4648` n `238`; crypto_major avg `-0.287` n `8`; equity avg `-0.1999` n `156`; fx avg `-0.0024` n `6`; index avg `-0.0218` n `27`; metal avg `-0.0151` n `20`; unknown avg `0.5032` n `1238`
- 1h: commodity avg `0.1794` n `13`; crypto_alt avg `0.4628` n `238`; crypto_major avg `0.3659` n `8`; equity avg `-0.0563` n `156`; fx avg `0.0156` n `6`; index avg `-0.0137` n `27`; metal avg `0.0144` n `20`; unknown avg `-0.2954` n `1226`
- 4h: commodity avg `-0.2226` n `13`; crypto_alt avg `2.4036` n `238`; crypto_major avg `2.2148` n `8`; equity avg `0.9146` n `156`; fx avg `0.0973` n `6`; index avg `0.007` n `27`; metal avg `-0.0087` n `20`; unknown avg `26.1626` n `1132`
- 24h: commodity avg `-0.8936` n `13`; crypto_alt avg `1.563` n `238`; crypto_major avg `3.1591` n `8`; equity avg `-0.3103` n `155`; fx avg `0.0254` n `6`; index avg `-0.1169` n `27`; metal avg `-0.444` n `20`; unknown avg `43.6784` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
