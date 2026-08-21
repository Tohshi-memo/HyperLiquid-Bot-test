# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T17:51:16.847245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `0.0316` n `230`; crypto_major avg `0.0489` n `8`; equity avg `-0.0248` n `121`; fx avg `-0.001` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0651` n `20`; unknown avg `-0.0568` n `793`
- 1h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.2564` n `230`; crypto_major avg `-0.2458` n `8`; equity avg `0.0265` n `121`; fx avg `0.0129` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0837` n `20`; unknown avg `-0.2371` n `793`
- 4h: commodity avg `0.1384` n `12`; crypto_alt avg `0.3425` n `230`; crypto_major avg `-0.1413` n `8`; equity avg `-0.3078` n `121`; fx avg `0.0179` n `6`; index avg `0.0168` n `25`; metal avg `0.0177` n `20`; unknown avg `0.0597` n `793`
- 24h: commodity avg `0.3013` n `12`; crypto_alt avg `6.647` n `230`; crypto_major avg `3.2572` n `8`; equity avg `1.2103` n `121`; fx avg `-0.0956` n `6`; index avg `0.0935` n `25`; metal avg `0.5705` n `20`; unknown avg `1.0265` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
