# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T20:37:27.285176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0354` n `13`; crypto_alt avg `0.2002` n `235`; crypto_major avg `0.133` n `8`; equity avg `0.0041` n `151`; fx avg `-0.0042` n `6`; index avg `-0.0007` n `26`; metal avg `0.0006` n `20`; unknown avg `-0.0141` n `1135`
- 1h: commodity avg `0.0854` n `13`; crypto_alt avg `0.2132` n `235`; crypto_major avg `0.0153` n `8`; equity avg `0.1696` n `151`; fx avg `-0.0069` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0621` n `20`; unknown avg `0.0362` n `1081`
- 4h: commodity avg `0.2709` n `13`; crypto_alt avg `0.3951` n `235`; crypto_major avg `-0.0414` n `8`; equity avg `0.1264` n `151`; fx avg `0.0245` n `6`; index avg `0.0082` n `26`; metal avg `-0.0236` n `20`; unknown avg `0.356` n `1081`
- 24h: commodity avg `0.9433` n `13`; crypto_alt avg `-1.386` n `235`; crypto_major avg `-0.6416` n `8`; equity avg `-0.7115` n `151`; fx avg `0.1751` n `6`; index avg `-0.144` n `26`; metal avg `-0.2827` n `20`; unknown avg `0.2897` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1576`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.092`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
