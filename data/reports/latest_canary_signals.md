# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T01:16:03.479050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `0.0155` n `230`; crypto_major avg `-0.0341` n `8`; equity avg `-0.066` n `94`; fx avg `0.0018` n `6`; index avg `0.0108` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.069` n `768`
- 1h: commodity avg `0.0936` n `12`; crypto_alt avg `0.339` n `230`; crypto_major avg `0.3275` n `8`; equity avg `0.0799` n `94`; fx avg `-0.0353` n `6`; index avg `0.0139` n `25`; metal avg `0.0586` n `20`; unknown avg `0.016` n `768`
- 4h: commodity avg `0.077` n `12`; crypto_alt avg `-0.6056` n `230`; crypto_major avg `-0.4995` n `8`; equity avg `-0.8899` n `94`; fx avg `-0.0148` n `6`; index avg `-0.1457` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.4489` n `768`
- 24h: commodity avg `-0.055` n `12`; crypto_alt avg `-1.0401` n `230`; crypto_major avg `-1.8699` n `8`; equity avg `-3.9183` n `94`; fx avg `-0.184` n `6`; index avg `-0.4477` n `25`; metal avg `-0.5883` n `20`; unknown avg `-0.5682` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
