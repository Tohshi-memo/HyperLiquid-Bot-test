# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T09:37:23.991134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5088` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1915` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.0871` n `231`; crypto_major avg `-0.0459` n `8`; equity avg `0.0165` n `127`; fx avg `0.0121` n `6`; index avg `0.0182` n `26`; metal avg `-0.0639` n `20`; unknown avg `0.0964` n `792`
- 1h: commodity avg `0.1283` n `12`; crypto_alt avg `0.1895` n `231`; crypto_major avg `0.487` n `8`; equity avg `0.0212` n `127`; fx avg `0.011` n `6`; index avg `-0.0083` n `26`; metal avg `-0.093` n `20`; unknown avg `-0.0392` n `792`
- 4h: commodity avg `0.0718` n `12`; crypto_alt avg `2.2228` n `231`; crypto_major avg `2.2633` n `8`; equity avg `0.8769` n `127`; fx avg `0.0007` n `6`; index avg `0.1078` n `26`; metal avg `-0.2455` n `20`; unknown avg `0.3366` n `775`
- 24h: commodity avg `0.499` n `12`; crypto_alt avg `2.5528` n `231`; crypto_major avg `3.1138` n `8`; equity avg `2.1429` n `127`; fx avg `-0.081` n `6`; index avg `0.318` n `26`; metal avg `-0.4064` n `20`; unknown avg `0.6088` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
