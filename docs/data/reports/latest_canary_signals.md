# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T12:22:25.916064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0751` n `12`; crypto_alt avg `-0.0472` n `230`; crypto_major avg `-0.0801` n `8`; equity avg `-0.0084` n `96`; fx avg `0.0` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0169` n `20`; unknown avg `0.0133` n `769`
- 1h: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.0534` n `230`; crypto_major avg `-0.0604` n `8`; equity avg `-0.2444` n `96`; fx avg `-0.01` n `6`; index avg `-0.0343` n `25`; metal avg `-0.0774` n `20`; unknown avg `0.1309` n `769`
- 4h: commodity avg `0.2477` n `12`; crypto_alt avg `0.38` n `230`; crypto_major avg `0.4001` n `8`; equity avg `0.8834` n `96`; fx avg `-0.014` n `6`; index avg `0.1046` n `25`; metal avg `-0.0405` n `20`; unknown avg `0.1917` n `768`
- 24h: commodity avg `-0.2096` n `12`; crypto_alt avg `-1.4919` n `230`; crypto_major avg `-2.6209` n `8`; equity avg `-4.5588` n `94`; fx avg `-0.0539` n `6`; index avg `-0.5609` n `25`; metal avg `-0.7002` n `20`; unknown avg `-0.3794` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
