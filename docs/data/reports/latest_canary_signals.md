# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T02:37:30.313855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `0.0002` n `236`; crypto_major avg `0.0154` n `8`; equity avg `0.0978` n `151`; fx avg `-0.0144` n `6`; index avg `0.017` n `26`; metal avg `0.0945` n `20`; unknown avg `-0.1684` n `1136`
- 1h: commodity avg `-0.1442` n `13`; crypto_alt avg `0.1331` n `236`; crypto_major avg `0.1763` n `8`; equity avg `0.2173` n `151`; fx avg `-0.0325` n `6`; index avg `0.0513` n `26`; metal avg `0.1813` n `20`; unknown avg `-0.0139` n `1134`
- 4h: commodity avg `-0.1808` n `13`; crypto_alt avg `-0.236` n `236`; crypto_major avg `-0.359` n `8`; equity avg `0.0701` n `151`; fx avg `0.0386` n `6`; index avg `0.0055` n `26`; metal avg `0.0799` n `20`; unknown avg `0.3547` n `1128`
- 24h: commodity avg `-0.1291` n `13`; crypto_alt avg `3.4109` n `236`; crypto_major avg `1.7447` n `8`; equity avg `2.0755` n `151`; fx avg `-0.0047` n `6`; index avg `0.3665` n `26`; metal avg `0.4195` n `20`; unknown avg `25.7147` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0894`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0758`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0705`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
