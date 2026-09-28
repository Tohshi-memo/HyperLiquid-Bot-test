# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T00:52:25.238870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.4287` n `234`; crypto_major avg `0.3963` n `8`; equity avg `0.0117` n `141`; fx avg `-0.0139` n `6`; index avg `0.0173` n `26`; metal avg `-0.0251` n `20`; unknown avg `24.4309` n `962`
- 1h: commodity avg `-0.0733` n `12`; crypto_alt avg `0.0621` n `234`; crypto_major avg `-0.0038` n `8`; equity avg `-0.2052` n `141`; fx avg `0.0806` n `6`; index avg `0.0298` n `26`; metal avg `-0.2071` n `20`; unknown avg `57.665` n `954`
- 4h: commodity avg `-0.4199` n `12`; crypto_alt avg `0.5267` n `234`; crypto_major avg `-0.0192` n `8`; equity avg `-0.5384` n `141`; fx avg `0.065` n `6`; index avg `-0.029` n `26`; metal avg `-0.3618` n `20`; unknown avg `3.7681` n `886`
- 24h: commodity avg `-0.4618` n `12`; crypto_alt avg `1.3969` n `234`; crypto_major avg `0.271` n `8`; equity avg `-0.2369` n `141`; fx avg `0.0423` n `6`; index avg `0.0115` n `26`; metal avg `-0.3768` n `20`; unknown avg `11.0931` n `829`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
