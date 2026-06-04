# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T23:07:28.011647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `0.7502` n `228`; crypto_major avg `0.7198` n `8`; equity avg `-0.0337` n `74`; fx avg `0.0051` n `6`; index avg `0.0305` n `23`; metal avg `-0.0476` n `18`; unknown avg `-0.0097` n `424`
- 1h: commodity avg `0.0525` n `12`; crypto_alt avg `0.9844` n `228`; crypto_major avg `0.9374` n `8`; equity avg `-0.2006` n `74`; fx avg `0.0006` n `6`; index avg `-0.1074` n `23`; metal avg `-0.0223` n `18`; unknown avg `0.341` n `424`
- 4h: commodity avg `-0.1311` n `12`; crypto_alt avg `-1.6759` n `228`; crypto_major avg `-0.5568` n `8`; equity avg `-0.9652` n `74`; fx avg `-0.0172` n `6`; index avg `-0.3746` n `23`; metal avg `-0.2215` n `18`; unknown avg `-0.7917` n `424`
- 24h: commodity avg `-0.4482` n `12`; crypto_alt avg `-6.1177` n `228`; crypto_major avg `-3.6847` n `8`; equity avg `-0.1365` n `73`; fx avg `0.0395` n `6`; index avg `0.1893` n `23`; metal avg `0.7135` n `18`; unknown avg `-1.6031` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
