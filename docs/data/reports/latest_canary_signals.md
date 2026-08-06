# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T02:37:24.867309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0021` n `230`; crypto_major avg `-0.122` n `8`; equity avg `0.0806` n `108`; fx avg `0.0279` n `6`; index avg `0.0102` n `25`; metal avg `-0.0701` n `20`; unknown avg `-0.0188` n `782`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.3111` n `230`; crypto_major avg `-0.5893` n `8`; equity avg `0.6503` n `108`; fx avg `0.0348` n `6`; index avg `0.0631` n `25`; metal avg `0.0238` n `20`; unknown avg `0.394` n `782`
- 4h: commodity avg `0.1277` n `12`; crypto_alt avg `-0.315` n `230`; crypto_major avg `-0.764` n `8`; equity avg `-0.2921` n `108`; fx avg `-0.0383` n `6`; index avg `-0.1861` n `25`; metal avg `0.2066` n `20`; unknown avg `0.1091` n `782`
- 24h: commodity avg `0.2505` n `12`; crypto_alt avg `-0.2716` n `230`; crypto_major avg `-0.6604` n `8`; equity avg `-1.4125` n `108`; fx avg `0.0103` n `6`; index avg `-0.2976` n `25`; metal avg `0.7038` n `20`; unknown avg `0.8783` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
