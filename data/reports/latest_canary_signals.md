# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T15:07:25.865725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4395` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.3451` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.4522` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `0.1577` n `239`; crypto_major avg `0.1538` n `8`; equity avg `0.1276` n `166`; fx avg `-0.002` n `6`; index avg `0.0061` n `27`; metal avg `0.0118` n `20`; unknown avg `200.5555` n `1254`
- 1h: commodity avg `-0.0004` n `13`; crypto_alt avg `0.3121` n `239`; crypto_major avg `0.0606` n `8`; equity avg `-0.0569` n `166`; fx avg `0.0039` n `6`; index avg `-0.0268` n `27`; metal avg `0.0051` n `20`; unknown avg `398.1092` n `1258`
- 4h: commodity avg `0.0677` n `13`; crypto_alt avg `3.0071` n `239`; crypto_major avg `3.5072` n `8`; equity avg `1.055` n `166`; fx avg `0.0126` n `6`; index avg `0.1036` n `27`; metal avg `0.1621` n `20`; unknown avg `207.0372` n `1220`
- 24h: commodity avg `0.6325` n `13`; crypto_alt avg `-1.3769` n `239`; crypto_major avg `-1.3048` n `8`; equity avg `-3.7421` n `166`; fx avg `-0.0837` n `6`; index avg `-0.4641` n `27`; metal avg `-0.2429` n `20`; unknown avg `0.6362` n `1147`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
