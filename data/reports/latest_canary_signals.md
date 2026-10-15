# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T19:22:36.383732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0505` n `13`; crypto_alt avg `0.0597` n `236`; crypto_major avg `0.125` n `8`; equity avg `0.5597` n `151`; fx avg `0.0018` n `6`; index avg `0.0737` n `26`; metal avg `0.0139` n `20`; unknown avg `1.2667` n `1136`
- 1h: commodity avg `-0.1321` n `13`; crypto_alt avg `0.6229` n `236`; crypto_major avg `0.5743` n `8`; equity avg `1.2606` n `151`; fx avg `-0.0079` n `6`; index avg `0.1755` n `26`; metal avg `0.0272` n `20`; unknown avg `2.8629` n `1134`
- 4h: commodity avg `-0.0927` n `13`; crypto_alt avg `1.5187` n `236`; crypto_major avg `0.8458` n `8`; equity avg `1.1392` n `151`; fx avg `0.0154` n `6`; index avg `0.1363` n `26`; metal avg `0.002` n `20`; unknown avg `0.254` n `1128`
- 24h: commodity avg `-0.0946` n `13`; crypto_alt avg `1.1353` n `236`; crypto_major avg `0.7399` n `8`; equity avg `-0.1955` n `151`; fx avg `0.1869` n `6`; index avg `-0.0917` n `26`; metal avg `0.3998` n `20`; unknown avg `0.6337` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0836`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0551`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0524`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
