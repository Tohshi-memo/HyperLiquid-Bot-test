# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T13:22:28.538107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0506` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6965` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0517` n `12`; crypto_alt avg `0.0917` n `231`; crypto_major avg `0.0509` n `8`; equity avg `-0.0175` n `122`; fx avg `0.0078` n `6`; index avg `0.0066` n `25`; metal avg `-0.0249` n `20`; unknown avg `-0.1488` n `793`
- 1h: commodity avg `0.0377` n `12`; crypto_alt avg `0.8533` n `231`; crypto_major avg `0.8515` n `8`; equity avg `-0.115` n `122`; fx avg `0.0225` n `6`; index avg `-0.0288` n `25`; metal avg `0.1049` n `20`; unknown avg `0.4522` n `793`
- 4h: commodity avg `0.201` n `12`; crypto_alt avg `1.4103` n `231`; crypto_major avg `1.9257` n `8`; equity avg `-0.1249` n `122`; fx avg `0.0196` n `6`; index avg `-0.0271` n `25`; metal avg `0.2292` n `20`; unknown avg `1.0268` n `793`
- 24h: commodity avg `0.0236` n `12`; crypto_alt avg `1.0671` n `231`; crypto_major avg `0.8487` n `8`; equity avg `-1.6804` n `122`; fx avg `-0.1138` n `6`; index avg `-0.1668` n `25`; metal avg `0.2831` n `20`; unknown avg `4.1129` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
