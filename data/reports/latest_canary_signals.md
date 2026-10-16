# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T14:52:30.046572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `13`; crypto_alt avg `0.1418` n `236`; crypto_major avg `-0.1468` n `8`; equity avg `-0.1694` n `151`; fx avg `-0.0048` n `6`; index avg `0.0041` n `26`; metal avg `0.0152` n `20`; unknown avg `-0.0286` n `1088`
- 1h: commodity avg `-0.1105` n `13`; crypto_alt avg `0.4325` n `236`; crypto_major avg `0.4276` n `8`; equity avg `0.1931` n `151`; fx avg `0.0209` n `6`; index avg `0.0439` n `26`; metal avg `0.0126` n `20`; unknown avg `2.5797` n `1020`
- 4h: commodity avg `-0.3693` n `13`; crypto_alt avg `-0.0435` n `236`; crypto_major avg `-0.2902` n `8`; equity avg `-1.464` n `151`; fx avg `0.0219` n `6`; index avg `-0.1267` n `26`; metal avg `0.0339` n `20`; unknown avg `1.9832` n `1012`
- 24h: commodity avg `-0.4126` n `13`; crypto_alt avg `2.6754` n `236`; crypto_major avg `1.2964` n `8`; equity avg `0.3983` n `151`; fx avg `0.0564` n `6`; index avg `0.033` n `26`; metal avg `0.2156` n `20`; unknown avg `-0.0347` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1028`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0992`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0821`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
