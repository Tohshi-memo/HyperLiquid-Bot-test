# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T04:37:35.693086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.026` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `0.0816` n `239`; crypto_major avg `0.0292` n `8`; equity avg `0.1684` n `168`; fx avg `-0.0155` n `6`; index avg `0.0115` n `27`; metal avg `-0.0108` n `20`; unknown avg `10.103` n `1263`
- 1h: commodity avg `0.056` n `13`; crypto_alt avg `-0.0375` n `239`; crypto_major avg `-0.0106` n `8`; equity avg `0.3101` n `168`; fx avg `-0.0156` n `6`; index avg `0.0532` n `27`; metal avg `0.0062` n `20`; unknown avg `66.541` n `1255`
- 4h: commodity avg `0.1503` n `13`; crypto_alt avg `1.4315` n `239`; crypto_major avg `2.1763` n `8`; equity avg `3.0275` n `168`; fx avg `-0.0131` n `6`; index avg `0.3191` n `27`; metal avg `0.9098` n `20`; unknown avg `2.7243` n `1247`
- 24h: commodity avg `0.2283` n `13`; crypto_alt avg `1.6032` n `239`; crypto_major avg `1.8146` n `8`; equity avg `2.2892` n `168`; fx avg `0.0116` n `6`; index avg `0.2338` n `27`; metal avg `0.6165` n `20`; unknown avg `205.7212` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
