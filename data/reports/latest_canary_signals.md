# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T06:52:32.275200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `13`; crypto_alt avg `0.0307` n `235`; crypto_major avg `0.0031` n `8`; equity avg `-0.0405` n `151`; fx avg `-0.0069` n `6`; index avg `0.0456` n `26`; metal avg `-0.016` n `20`; unknown avg `-0.082` n `1135`
- 1h: commodity avg `-0.0491` n `13`; crypto_alt avg `0.2233` n `235`; crypto_major avg `0.1363` n `8`; equity avg `0.0176` n `151`; fx avg `-0.0191` n `6`; index avg `0.0162` n `26`; metal avg `-0.0411` n `20`; unknown avg `0.2469` n `1117`
- 4h: commodity avg `-0.1624` n `13`; crypto_alt avg `-0.6162` n `235`; crypto_major avg `-0.297` n `8`; equity avg `-0.8248` n `151`; fx avg `-0.0013` n `6`; index avg `-0.0909` n `26`; metal avg `-0.0802` n `20`; unknown avg `0.1094` n `1111`
- 24h: commodity avg `0.9513` n `13`; crypto_alt avg `-1.3614` n `235`; crypto_major avg `-0.7386` n `8`; equity avg `-0.0685` n `151`; fx avg `0.0416` n `6`; index avg `0.0336` n `26`; metal avg `-0.3945` n `20`; unknown avg `0.4464` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1564`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1384`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0833`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0706`, n `666`, weak_sample_signal
