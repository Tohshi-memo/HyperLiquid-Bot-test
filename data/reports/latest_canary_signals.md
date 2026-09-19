# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T19:22:36.114501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `-0.0364` n `234`; crypto_major avg `-0.0784` n `8`; equity avg `0.0118` n `140`; fx avg `-0.0032` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0045` n `20`; unknown avg `1.8458` n `943`
- 1h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.0286` n `234`; crypto_major avg `0.033` n `8`; equity avg `0.029` n `140`; fx avg `-0.0012` n `6`; index avg `-0.0035` n `26`; metal avg `0.0067` n `20`; unknown avg `3.489` n `941`
- 4h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0783` n `234`; crypto_major avg `-0.2627` n `8`; equity avg `0.0664` n `140`; fx avg `-0.0045` n `6`; index avg `0.0169` n `26`; metal avg `-0.0024` n `20`; unknown avg `18.2804` n `883`
- 24h: commodity avg `0.08` n `12`; crypto_alt avg `1.6578` n `234`; crypto_major avg `0.3272` n `8`; equity avg `0.2102` n `140`; fx avg `0.0098` n `6`; index avg `0.0713` n `26`; metal avg `-0.0436` n `20`; unknown avg `6.9726` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
