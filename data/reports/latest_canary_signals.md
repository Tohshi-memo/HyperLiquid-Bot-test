# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T20:22:29.630028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0957` n `13`; crypto_alt avg `-0.1572` n `236`; crypto_major avg `-0.0373` n `8`; equity avg `-0.0198` n `151`; fx avg `0.0018` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0076` n `20`; unknown avg `-0.0699` n `1193`
- 1h: commodity avg `-0.0739` n `13`; crypto_alt avg `0.0294` n `236`; crypto_major avg `0.1437` n `8`; equity avg `-0.0225` n `151`; fx avg `-0.003` n `6`; index avg `-0.0026` n `26`; metal avg `0.0019` n `20`; unknown avg `0.0573` n `1153`
- 4h: commodity avg `-0.0417` n `13`; crypto_alt avg `0.5566` n `236`; crypto_major avg `0.4907` n `8`; equity avg `0.1201` n `151`; fx avg `-0.0048` n `6`; index avg `0.0172` n `26`; metal avg `0.0052` n `20`; unknown avg `1.4167` n `1105`
- 24h: commodity avg `0.0273` n `13`; crypto_alt avg `-0.8312` n `236`; crypto_major avg `0.0044` n `8`; equity avg `-0.1266` n `151`; fx avg `-0.0298` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0215` n `20`; unknown avg `4.4161` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1713`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1482`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
