# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T19:37:28.011423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0992` n `13`; crypto_alt avg `-0.2599` n `239`; crypto_major avg `-0.0838` n `8`; equity avg `-0.1757` n `162`; fx avg `-0.0047` n `6`; index avg `-0.0187` n `27`; metal avg `-0.0106` n `20`; unknown avg `301.2268` n `1261`
- 1h: commodity avg `0.2263` n `13`; crypto_alt avg `-0.0868` n `239`; crypto_major avg `-0.341` n `8`; equity avg `-0.5797` n `162`; fx avg `0.0186` n `6`; index avg `-0.0567` n `27`; metal avg `-0.059` n `20`; unknown avg `1.0125` n `1255`
- 4h: commodity avg `0.6288` n `13`; crypto_alt avg `1.0164` n `239`; crypto_major avg `0.623` n `8`; equity avg `0.6228` n `162`; fx avg `-0.0052` n `6`; index avg `0.04` n `27`; metal avg `0.1404` n `20`; unknown avg `53.597` n `1229`
- 24h: commodity avg `0.9557` n `13`; crypto_alt avg `-2.6793` n `239`; crypto_major avg `-3.1567` n `8`; equity avg `-2.8315` n `162`; fx avg `-0.1449` n `6`; index avg `-0.1868` n `27`; metal avg `-0.7851` n `20`; unknown avg `6.5638` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
