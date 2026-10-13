# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T16:22:28.515789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.3136` n `235`; crypto_major avg `0.1748` n `8`; equity avg `0.1934` n `151`; fx avg `0.0025` n `6`; index avg `0.0225` n `26`; metal avg `0.0006` n `20`; unknown avg `0.4129` n `1135`
- 1h: commodity avg `0.0699` n `13`; crypto_alt avg `-0.0008` n `235`; crypto_major avg `-0.0025` n `8`; equity avg `0.3665` n `151`; fx avg `-0.0088` n `6`; index avg `0.0425` n `26`; metal avg `-0.089` n `20`; unknown avg `0.8388` n `1127`
- 4h: commodity avg `0.7381` n `13`; crypto_alt avg `1.3601` n `235`; crypto_major avg `0.9933` n `8`; equity avg `0.5693` n `151`; fx avg `0.0343` n `6`; index avg `0.0417` n `26`; metal avg `-0.2743` n `20`; unknown avg `0.7883` n `1091`
- 24h: commodity avg `0.4174` n `13`; crypto_alt avg `-2.0279` n `235`; crypto_major avg `-0.7189` n `8`; equity avg `-1.2677` n `151`; fx avg `0.1561` n `6`; index avg `-0.2513` n `26`; metal avg `-0.2691` n `20`; unknown avg `0.1569` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1625`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1478`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0928`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
