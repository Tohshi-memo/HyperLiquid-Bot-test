# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T01:52:25.829789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `0.3211` n `235`; crypto_major avg `0.2182` n `8`; equity avg `0.1824` n `151`; fx avg `-0.018` n `6`; index avg `0.033` n `26`; metal avg `0.0618` n `20`; unknown avg `0.6479` n `1135`
- 1h: commodity avg `-0.0088` n `13`; crypto_alt avg `-0.0277` n `235`; crypto_major avg `-0.0535` n `8`; equity avg `-0.1137` n `151`; fx avg `-0.012` n `6`; index avg `0.0093` n `26`; metal avg `0.0015` n `20`; unknown avg `-0.025` n `1133`
- 4h: commodity avg `0.1638` n `13`; crypto_alt avg `-0.0009` n `235`; crypto_major avg `0.068` n `8`; equity avg `0.0344` n `151`; fx avg `0.0166` n `6`; index avg `0.0179` n `26`; metal avg `-0.0889` n `20`; unknown avg `0.5286` n `1071`
- 24h: commodity avg `1.0285` n `13`; crypto_alt avg `1.577` n `235`; crypto_major avg `1.3403` n `8`; equity avg `0.8771` n `151`; fx avg `0.1211` n `6`; index avg `0.156` n `26`; metal avg `-0.1665` n `20`; unknown avg `1.5438` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1561`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0942`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `666`, weak_sample_signal
