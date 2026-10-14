# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T09:37:29.335689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0882` n `13`; crypto_alt avg `-0.3787` n `235`; crypto_major avg `-0.2049` n `8`; equity avg `-0.1225` n `151`; fx avg `-0.0017` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0252` n `20`; unknown avg `-0.1861` n `1135`
- 1h: commodity avg `0.0622` n `13`; crypto_alt avg `-0.8093` n `235`; crypto_major avg `-0.4977` n `8`; equity avg `-0.2989` n `151`; fx avg `0.003` n `6`; index avg `-0.0152` n `26`; metal avg `-0.0825` n `20`; unknown avg `0.5243` n `1053`
- 4h: commodity avg `0.0196` n `13`; crypto_alt avg `-0.7408` n `235`; crypto_major avg `-0.3318` n `8`; equity avg `-0.3083` n `151`; fx avg `-0.0439` n `6`; index avg `-0.006` n `26`; metal avg `-0.1832` n `20`; unknown avg `1149.2571` n `1021`
- 24h: commodity avg `1.1457` n `13`; crypto_alt avg `-1.0512` n `235`; crypto_major avg `-0.3953` n `8`; equity avg `-0.6728` n `151`; fx avg `0.0299` n `6`; index avg `-0.0342` n `26`; metal avg `-0.5154` n `20`; unknown avg `1203.1254` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1321`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0744`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0729`, n `666`, weak_sample_signal
