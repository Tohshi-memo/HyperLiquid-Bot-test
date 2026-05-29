# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T18:07:22.460734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.035` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4244` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7973` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0713` n `12`; crypto_alt avg `0.0276` n `228`; crypto_major avg `0.013` n `8`; equity avg `-0.0533` n `69`; fx avg `-0.0011` n `6`; index avg `-0.0171` n `23`; metal avg `0.0763` n `18`; unknown avg `0.0542` n `419`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `0.2094` n `228`; crypto_major avg `-0.0684` n `8`; equity avg `-0.1503` n `69`; fx avg `-0.0135` n `6`; index avg `-0.1447` n `23`; metal avg `-0.1794` n `18`; unknown avg `1.0855` n `419`
- 4h: commodity avg `-0.7894` n `12`; crypto_alt avg `2.2925` n `228`; crypto_major avg `2.2456` n `8`; equity avg `0.4483` n `69`; fx avg `0.0812` n `6`; index avg `-0.1127` n `23`; metal avg `-0.1788` n `18`; unknown avg `2.0881` n `417`
- 24h: commodity avg `-0.5658` n `12`; crypto_alt avg `1.0029` n `228`; crypto_major avg `1.4967` n `8`; equity avg `1.5032` n `69`; fx avg `0.2035` n `6`; index avg `-0.1477` n `23`; metal avg `-0.0591` n `18`; unknown avg `1.9916` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
