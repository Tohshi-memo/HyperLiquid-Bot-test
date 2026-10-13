# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T21:22:31.444774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `-0.2035` n `235`; crypto_major avg `-0.1041` n `8`; equity avg `-0.0203` n `151`; fx avg `0.0086` n `6`; index avg `0.0063` n `26`; metal avg `0.0006` n `20`; unknown avg `0.227` n `1135`
- 1h: commodity avg `-0.0752` n `13`; crypto_alt avg `-0.0187` n `235`; crypto_major avg `0.0548` n `8`; equity avg `0.0204` n `151`; fx avg `-0.0181` n `6`; index avg `0.0192` n `26`; metal avg `0.0351` n `20`; unknown avg `0.0426` n `1127`
- 4h: commodity avg `0.1662` n `13`; crypto_alt avg `0.2553` n `235`; crypto_major avg `0.0144` n `8`; equity avg `0.4704` n `151`; fx avg `0.006` n `6`; index avg `0.0587` n `26`; metal avg `0.0154` n `20`; unknown avg `1.8551` n `1075`
- 24h: commodity avg `0.8477` n `13`; crypto_alt avg `-1.373` n `235`; crypto_major avg `-0.5235` n `8`; equity avg `-0.6773` n `151`; fx avg `0.1661` n `6`; index avg `-0.1465` n `26`; metal avg `-0.2857` n `20`; unknown avg `14.572` n `1019`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1578`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1427`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `666`, weak_sample_signal
