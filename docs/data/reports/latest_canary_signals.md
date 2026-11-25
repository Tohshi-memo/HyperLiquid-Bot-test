# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T19:22:29.191930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.6527` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.627` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.7572` n `239`; crypto_major avg `0.8253` n `8`; equity avg `-0.0348` n `168`; fx avg `0.0055` n `6`; index avg `-0.0149` n `27`; metal avg `-0.0287` n `20`; unknown avg `0.2325` n `1265`
- 1h: commodity avg `-0.0723` n `13`; crypto_alt avg `1.278` n `239`; crypto_major avg `1.4554` n `8`; equity avg `1.5348` n `168`; fx avg `0.0137` n `6`; index avg `0.1216` n `27`; metal avg `0.276` n `20`; unknown avg `1.0986` n `1263`
- 4h: commodity avg `0.1521` n `13`; crypto_alt avg `4.7442` n `239`; crypto_major avg `4.8048` n `8`; equity avg `5.4749` n `168`; fx avg `0.0865` n `6`; index avg `0.523` n `27`; metal avg `1.1778` n `20`; unknown avg `173.903` n `1256`
- 24h: commodity avg `0.3101` n `13`; crypto_alt avg `2.1311` n `239`; crypto_major avg `1.4857` n `8`; equity avg `-0.6937` n `168`; fx avg `0.0323` n `6`; index avg `-0.1027` n `27`; metal avg `-0.0292` n `20`; unknown avg `2.4325` n `1087`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
