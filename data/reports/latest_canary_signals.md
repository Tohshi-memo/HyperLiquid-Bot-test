# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T02:37:26.100968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.7662` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.417` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1898` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.2525` n `231`; crypto_major avg `0.3468` n `8`; equity avg `0.0159` n `122`; fx avg `-0.0017` n `6`; index avg `0.02` n `25`; metal avg `-0.0799` n `20`; unknown avg `-0.0666` n `794`
- 1h: commodity avg `0.1037` n `12`; crypto_alt avg `0.8926` n `231`; crypto_major avg `0.9747` n `8`; equity avg `0.2214` n `122`; fx avg `-0.002` n `6`; index avg `0.0409` n `25`; metal avg `-0.2675` n `20`; unknown avg `-0.0496` n `794`
- 4h: commodity avg `0.1444` n `12`; crypto_alt avg `1.7214` n `231`; crypto_major avg `2.5614` n `8`; equity avg `0.3716` n `122`; fx avg `0.0261` n `6`; index avg `0.0256` n `25`; metal avg `-0.2048` n `20`; unknown avg `0.3545` n `794`
- 24h: commodity avg `0.1149` n `12`; crypto_alt avg `1.6102` n `231`; crypto_major avg `2.3837` n `8`; equity avg `-1.4305` n `122`; fx avg `0.0268` n `6`; index avg `-0.2538` n `25`; metal avg `-0.1499` n `20`; unknown avg `0.5387` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
