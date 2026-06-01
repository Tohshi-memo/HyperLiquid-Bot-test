# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T17:22:25.149162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5832` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1591` n `12`; crypto_alt avg `-0.2435` n `228`; crypto_major avg `-0.0931` n `8`; equity avg `-0.0208` n `69`; fx avg `-0.0041` n `6`; index avg `0.1452` n `23`; metal avg `0.0047` n `18`; unknown avg `-0.3763` n `422`
- 1h: commodity avg `-0.6197` n `12`; crypto_alt avg `1.0588` n `228`; crypto_major avg `1.0518` n `8`; equity avg `0.4772` n `69`; fx avg `0.0171` n `6`; index avg `0.2245` n `23`; metal avg `0.1773` n `18`; unknown avg `0.3255` n `422`
- 4h: commodity avg `0.0006` n `12`; crypto_alt avg `1.2053` n `228`; crypto_major avg `-0.2645` n `8`; equity avg `1.3187` n `69`; fx avg `0.0263` n `6`; index avg `0.3682` n `23`; metal avg `0.3134` n `18`; unknown avg `-0.0972` n `422`
- 24h: commodity avg `0.5627` n `12`; crypto_alt avg `1.599` n `228`; crypto_major avg `-0.5801` n `8`; equity avg `0.3963` n `69`; fx avg `0.019` n `6`; index avg `0.3711` n `23`; metal avg `-0.1604` n `18`; unknown avg `3.805` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.289`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2236`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
