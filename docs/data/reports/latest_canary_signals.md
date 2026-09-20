# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T18:22:29.736274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7471` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `0.0838` n `234`; crypto_major avg `0.1825` n `8`; equity avg `-0.0037` n `140`; fx avg `0.0088` n `6`; index avg `0.0009` n `26`; metal avg `-0.01` n `20`; unknown avg `166.2777` n `943`
- 1h: commodity avg `-0.0138` n `12`; crypto_alt avg `0.1302` n `234`; crypto_major avg `0.1009` n `8`; equity avg `-0.047` n `140`; fx avg `-0.0098` n `6`; index avg `-0.001` n `26`; metal avg `-0.0212` n `20`; unknown avg `40.2502` n `941`
- 4h: commodity avg `-0.0092` n `12`; crypto_alt avg `2.9355` n `234`; crypto_major avg `1.7413` n `8`; equity avg `0.2911` n `140`; fx avg `0.0182` n `6`; index avg `0.0366` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.6765` n `879`
- 24h: commodity avg `0.3102` n `12`; crypto_alt avg `0.3882` n `234`; crypto_major avg `-0.5529` n `8`; equity avg `-0.0631` n `140`; fx avg `-0.0251` n `6`; index avg `-0.0429` n `26`; metal avg `-0.0328` n `20`; unknown avg `62.1313` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
