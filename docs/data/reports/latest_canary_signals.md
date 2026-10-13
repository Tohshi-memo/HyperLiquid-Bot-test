# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T14:07:37.265154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2369` n `13`; crypto_alt avg `0.3039` n `235`; crypto_major avg `0.3341` n `8`; equity avg `0.1576` n `151`; fx avg `0.0006` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0186` n `20`; unknown avg `0.7778` n `1133`
- 1h: commodity avg `0.4798` n `13`; crypto_alt avg `0.6321` n `235`; crypto_major avg `0.5946` n `8`; equity avg `0.5893` n `151`; fx avg `0.0259` n `6`; index avg `0.0771` n `26`; metal avg `-0.0512` n `20`; unknown avg `8.9775` n `1125`
- 4h: commodity avg `0.8985` n `13`; crypto_alt avg `-0.021` n `235`; crypto_major avg `0.1119` n `8`; equity avg `-0.3206` n `151`; fx avg `0.093` n `6`; index avg `-0.0317` n `26`; metal avg `-0.2609` n `20`; unknown avg `1.4861` n `1119`
- 24h: commodity avg `0.4855` n `13`; crypto_alt avg `-2.9206` n `235`; crypto_major avg `-1.3582` n `8`; equity avg `-1.5311` n `151`; fx avg `0.1008` n `6`; index avg `-0.2088` n `26`; metal avg `-0.2186` n `20`; unknown avg `0.5604` n `986`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1643`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1476`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1442`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1188`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
