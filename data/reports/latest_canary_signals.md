# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T04:22:30.887081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `13`; crypto_alt avg `-0.0459` n `235`; crypto_major avg `0.0009` n `8`; equity avg `-0.0851` n `151`; fx avg `0.0004` n `6`; index avg `-0.0007` n `26`; metal avg `0.0101` n `20`; unknown avg `-0.0637` n `1135`
- 1h: commodity avg `-0.0469` n `13`; crypto_alt avg `-0.1869` n `235`; crypto_major avg `-0.114` n `8`; equity avg `-0.1395` n `151`; fx avg `-0.0044` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0499` n `20`; unknown avg `-0.2862` n `1127`
- 4h: commodity avg `-0.067` n `13`; crypto_alt avg `-0.0589` n `235`; crypto_major avg `0.1893` n `8`; equity avg `0.0273` n `151`; fx avg `0.0258` n `6`; index avg `0.0491` n `26`; metal avg `0.0658` n `20`; unknown avg `-0.1038` n `1127`
- 24h: commodity avg `1.0901` n `13`; crypto_alt avg `0.0518` n `235`; crypto_major avg `0.1196` n `8`; equity avg `0.6305` n `151`; fx avg `0.0591` n `6`; index avg `0.1947` n `26`; metal avg `-0.3078` n `20`; unknown avg `1.343` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1527`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1364`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0876`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `666`, weak_sample_signal
