# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T03:37:38.904809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `0.0262` n `239`; crypto_major avg `-0.0155` n `8`; equity avg `0.2582` n `166`; fx avg `0.0138` n `6`; index avg `0.0001` n `27`; metal avg `0.0117` n `20`; unknown avg `0.5574` n `1264`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `1.3682` n `239`; crypto_major avg `1.6721` n `8`; equity avg `1.5415` n `166`; fx avg `0.0104` n `6`; index avg `0.1139` n `27`; metal avg `0.3365` n `20`; unknown avg `0.0358` n `1257`
- 4h: commodity avg `0.0178` n `13`; crypto_alt avg `0.5801` n `239`; crypto_major avg `0.5743` n `8`; equity avg `0.6909` n `166`; fx avg `0.0785` n `6`; index avg `0.0895` n `27`; metal avg `-0.0138` n `20`; unknown avg `-0.4493` n `1241`
- 24h: commodity avg `-0.3525` n `13`; crypto_alt avg `2.3407` n `239`; crypto_major avg `3.1548` n `8`; equity avg `2.2323` n `166`; fx avg `0.1917` n `6`; index avg `0.2398` n `27`; metal avg `0.4563` n `20`; unknown avg `245.4011` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
