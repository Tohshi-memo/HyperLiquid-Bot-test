# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T15:52:30.131049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0485` n `13`; crypto_alt avg `-0.3551` n `236`; crypto_major avg `-0.1965` n `8`; equity avg `-0.0446` n `151`; fx avg `0.0292` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0055` n `20`; unknown avg `2.5829` n `1193`
- 1h: commodity avg `0.0447` n `13`; crypto_alt avg `-1.0172` n `236`; crypto_major avg `-0.6591` n `8`; equity avg `-0.26` n `151`; fx avg `0.0149` n `6`; index avg `-0.0235` n `26`; metal avg `-0.0132` n `20`; unknown avg `3.3402` n `1183`
- 4h: commodity avg `0.082` n `13`; crypto_alt avg `-1.5851` n `236`; crypto_major avg `-0.7688` n `8`; equity avg `-0.3715` n `151`; fx avg `0.0041` n `6`; index avg `-0.0694` n `26`; metal avg `-0.0408` n `20`; unknown avg `5.5012` n `1167`
- 24h: commodity avg `0.6209` n `13`; crypto_alt avg `-2.5139` n `236`; crypto_major avg `-0.7943` n `8`; equity avg `-1.6929` n `151`; fx avg `0.0177` n `6`; index avg `-0.3309` n `26`; metal avg `-0.1145` n `20`; unknown avg `1.4124` n `1054`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1718`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1456`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.115`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0707`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
