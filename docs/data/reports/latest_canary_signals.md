# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T17:46:03.476231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9348` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.6721` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.1573` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0289` n `12`; crypto_alt avg `0.0971` n `230`; crypto_major avg `0.2126` n `8`; equity avg `0.1628` n `121`; fx avg `0.0139` n `6`; index avg `0.0055` n `25`; metal avg `0.0152` n `20`; unknown avg `0.239` n `792`
- 1h: commodity avg `-0.0992` n `12`; crypto_alt avg `-0.2974` n `230`; crypto_major avg `-0.3635` n `8`; equity avg `-0.3762` n `121`; fx avg `0.0122` n `6`; index avg `-0.0466` n `25`; metal avg `-0.0545` n `20`; unknown avg `0.7998` n `792`
- 4h: commodity avg `0.0088` n `12`; crypto_alt avg `2.4014` n `230`; crypto_major avg `3.9436` n `8`; equity avg `0.7863` n `121`; fx avg `0.0092` n `6`; index avg `-0.0008` n `25`; metal avg `0.2715` n `20`; unknown avg `0.3153` n `792`
- 24h: commodity avg `0.3163` n `12`; crypto_alt avg `2.6863` n `230`; crypto_major avg `4.6733` n `8`; equity avg `-0.3821` n `120`; fx avg `-0.1814` n `6`; index avg `-0.0173` n `25`; metal avg `0.8195` n `20`; unknown avg `0.4489` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
