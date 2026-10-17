# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T14:07:33.743059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1757` n `13`; crypto_alt avg `-0.0933` n `236`; crypto_major avg `-0.0325` n `8`; equity avg `-0.0053` n `151`; fx avg `-0.0044` n `6`; index avg `-0.0118` n `26`; metal avg `0.0001` n `20`; unknown avg `1.9547` n `1191`
- 1h: commodity avg `0.2012` n `13`; crypto_alt avg `-0.0447` n `236`; crypto_major avg `0.0246` n `8`; equity avg `0.0192` n `151`; fx avg `-0.0102` n `6`; index avg `-0.0068` n `26`; metal avg `0.0082` n `20`; unknown avg `-0.0993` n `1191`
- 4h: commodity avg `0.18` n `13`; crypto_alt avg `-1.0846` n `236`; crypto_major avg `-0.4863` n `8`; equity avg `-0.1392` n `151`; fx avg `-0.0061` n `6`; index avg `-0.0426` n `26`; metal avg `-0.0024` n `20`; unknown avg `2.6549` n `1183`
- 24h: commodity avg `0.8338` n `13`; crypto_alt avg `-2.7351` n `236`; crypto_major avg `-1.418` n `8`; equity avg `-2.1252` n `151`; fx avg `-0.0243` n `6`; index avg `-0.4017` n `26`; metal avg `-0.1814` n `20`; unknown avg `2.5768` n `950`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1742`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1446`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0624`, n `666`, weak_sample_signal
