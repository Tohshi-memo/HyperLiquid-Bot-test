# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T11:51:10.943785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.62` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0612` n `12`; crypto_alt avg `0.017` n `228`; crypto_major avg `0.0815` n `8`; equity avg `0.062` n `66`; fx avg `0.0016` n `6`; index avg `0.0212` n `23`; metal avg `0.1908` n `18`; unknown avg `-0.0221` n `386`
- 1h: commodity avg `-0.345` n `12`; crypto_alt avg `0.0059` n `228`; crypto_major avg `-0.0933` n `8`; equity avg `0.315` n `66`; fx avg `-0.0054` n `6`; index avg `0.1901` n `23`; metal avg `0.1495` n `18`; unknown avg `0.1435` n `386`
- 4h: commodity avg `0.2673` n `12`; crypto_alt avg `-0.9731` n `228`; crypto_major avg `-0.856` n `8`; equity avg `-0.0324` n `66`; fx avg `0.0426` n `6`; index avg `-0.1338` n `23`; metal avg `-0.0388` n `18`; unknown avg `0.6026` n `386`
- 24h: commodity avg `-1.4924` n `12`; crypto_alt avg `1.9109` n `228`; crypto_major avg `2.2558` n `8`; equity avg `1.2832` n `66`; fx avg `0.0533` n `6`; index avg `0.9821` n `23`; metal avg `-0.2324` n `18`; unknown avg `6.5124` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
