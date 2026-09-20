# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T21:37:25.684960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `0.1745` n `234`; crypto_major avg `0.0766` n `8`; equity avg `0.0078` n `140`; fx avg `-0.0063` n `6`; index avg `-0.0018` n `26`; metal avg `0.017` n `20`; unknown avg `2.6336` n `943`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.2379` n `234`; crypto_major avg `-0.2363` n `8`; equity avg `-0.0224` n `140`; fx avg `-0.0367` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0047` n `20`; unknown avg `2.9596` n `917`
- 4h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.1323` n `234`; crypto_major avg `-0.1609` n `8`; equity avg `0.0358` n `140`; fx avg `-0.0321` n `6`; index avg `0.0151` n `26`; metal avg `-0.0187` n `20`; unknown avg `1.3628` n `873`
- 24h: commodity avg `0.289` n `12`; crypto_alt avg `1.6136` n `234`; crypto_major avg `0.2085` n `8`; equity avg `-0.0763` n `140`; fx avg `-0.0332` n `6`; index avg `-0.0472` n `26`; metal avg `-0.0451` n `20`; unknown avg `3.0768` n `777`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
