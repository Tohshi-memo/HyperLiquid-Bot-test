# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T17:37:12.191747+00:00`
- Correlation status: `ready`
- Asset price records: `666`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6376` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `0.3834` n `228`; crypto_major avg `0.4827` n `8`; equity avg `0.2553` n `65`; fx avg `0.0041` n `5`; index avg `0.0956` n `23`; metal avg `0.0625` n `18`; unknown avg `0.4548` n `375`
- 1h: commodity avg `-0.2658` n `12`; crypto_alt avg `0.6888` n `228`; crypto_major avg `0.7384` n `8`; equity avg `0.4622` n `65`; fx avg `0.0133` n `5`; index avg `0.2953` n `23`; metal avg `0.1758` n `18`; unknown avg `0.246` n `375`
- 4h: commodity avg `0.376` n `12`; crypto_alt avg `2.1565` n `228`; crypto_major avg `1.3275` n `8`; equity avg `0.8899` n `65`; fx avg `0.0054` n `5`; index avg `0.6484` n `23`; metal avg `-0.3101` n `18`; unknown avg `0.2092` n `375`
- 24h: commodity avg `-0.0201` n `12`; crypto_alt avg `3.4562` n `228`; crypto_major avg `1.1087` n `8`; equity avg `2.7769` n `65`; fx avg `0.1626` n `5`; index avg `1.4586` n `23`; metal avg `0.6212` n `18`; unknown avg `0.5262` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1208`, n `658`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1165`, n `658`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.113`, n `662`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0985`, n `658`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `662`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0962`, n `658`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `662`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `662`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `662`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `662`, weak_sample_signal
