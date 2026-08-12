# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T16:22:27.704775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.003` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.0199` n `230`; crypto_major avg `-0.0161` n `8`; equity avg `0.1227` n `113`; fx avg `-0.0032` n `6`; index avg `0.0131` n `25`; metal avg `0.0183` n `20`; unknown avg `0.0226` n `786`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `0.0112` n `230`; crypto_major avg `0.1089` n `8`; equity avg `0.2125` n `113`; fx avg `-0.0016` n `6`; index avg `-0.0038` n `25`; metal avg `-0.061` n `20`; unknown avg `0.0102` n `786`
- 4h: commodity avg `-0.133` n `12`; crypto_alt avg `-0.633` n `230`; crypto_major avg `-0.8261` n `8`; equity avg `1.1769` n `113`; fx avg `-0.0103` n `6`; index avg `0.0967` n `25`; metal avg `-0.042` n `20`; unknown avg `0.2679` n `786`
- 24h: commodity avg `0.1354` n `12`; crypto_alt avg `-0.1414` n `230`; crypto_major avg `0.9036` n `8`; equity avg `3.5678` n `113`; fx avg `0.0318` n `6`; index avg `0.3488` n `25`; metal avg `0.2455` n `20`; unknown avg `0.053` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
