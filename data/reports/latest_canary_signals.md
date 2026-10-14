# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T03:22:31.460765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `-0.0091` n `235`; crypto_major avg `-0.0313` n `8`; equity avg `0.0336` n `151`; fx avg `-0.0144` n `6`; index avg `0.0136` n `26`; metal avg `0.0145` n `20`; unknown avg `0.059` n `1135`
- 1h: commodity avg `-0.0188` n `13`; crypto_alt avg `0.1506` n `235`; crypto_major avg `0.1938` n `8`; equity avg `0.0935` n `151`; fx avg `-0.0007` n `6`; index avg `0.0252` n `26`; metal avg `0.0702` n `20`; unknown avg `0.3904` n `1133`
- 4h: commodity avg `0.0313` n `13`; crypto_alt avg `0.6339` n `235`; crypto_major avg `0.6082` n `8`; equity avg `0.3761` n `151`; fx avg `-0.0089` n `6`; index avg `0.0901` n `26`; metal avg `0.1446` n `20`; unknown avg `0.721` n `1127`
- 24h: commodity avg `1.0026` n `13`; crypto_alt avg `1.0923` n `235`; crypto_major avg `0.8042` n `8`; equity avg `1.1078` n `151`; fx avg `0.0433` n `6`; index avg `0.246` n `26`; metal avg `-0.161` n `20`; unknown avg `0.7554` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.151`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1357`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0907`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `666`, weak_sample_signal
