# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T15:22:27.810080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7709` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7192` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.698` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1394` n `12`; crypto_alt avg `0.0222` n `230`; crypto_major avg `0.1092` n `8`; equity avg `0.1768` n `92`; fx avg `-0.0171` n `6`; index avg `0.0288` n `25`; metal avg `-0.0817` n `20`; unknown avg `-0.0969` n `766`
- 1h: commodity avg `-0.1135` n `12`; crypto_alt avg `0.2856` n `230`; crypto_major avg `0.4506` n `8`; equity avg `0.5326` n `92`; fx avg `-0.0129` n `6`; index avg `0.1387` n `25`; metal avg `0.071` n `20`; unknown avg `-0.1969` n `758`
- 4h: commodity avg `-0.3382` n `12`; crypto_alt avg `1.7386` n `230`; crypto_major avg `2.4327` n `8`; equity avg `0.7347` n `92`; fx avg `-0.0217` n `6`; index avg `0.2914` n `25`; metal avg `0.7135` n `20`; unknown avg `0.7837` n `758`
- 24h: commodity avg `0.7654` n `12`; crypto_alt avg `0.6971` n `230`; crypto_major avg `2.1377` n `8`; equity avg `-0.0253` n `92`; fx avg `-0.011` n `6`; index avg `0.1734` n `25`; metal avg `0.6619` n `20`; unknown avg `-0.2584` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
