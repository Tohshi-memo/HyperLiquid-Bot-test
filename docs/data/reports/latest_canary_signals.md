# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T03:07:28.322449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `13`; crypto_alt avg `-0.0038` n `235`; crypto_major avg `0.0959` n `8`; equity avg `-0.0413` n `151`; fx avg `0.0279` n `6`; index avg `-0.0028` n `26`; metal avg `0.014` n `20`; unknown avg `0.2206` n `1133`
- 1h: commodity avg `-0.082` n `13`; crypto_alt avg `0.1122` n `235`; crypto_major avg `0.2214` n `8`; equity avg `0.06` n `151`; fx avg `0.0273` n `6`; index avg `0.0082` n `26`; metal avg `0.0794` n `20`; unknown avg `0.1701` n `1133`
- 4h: commodity avg `0.0607` n `13`; crypto_alt avg `0.7117` n `235`; crypto_major avg `0.6495` n `8`; equity avg `0.2247` n `151`; fx avg `0.0025` n `6`; index avg `0.0643` n `26`; metal avg `0.0985` n `20`; unknown avg `0.4424` n `1127`
- 24h: commodity avg `1.1023` n `13`; crypto_alt avg `1.1536` n `235`; crypto_major avg `0.7407` n `8`; equity avg `1.1901` n `151`; fx avg `0.0625` n `6`; index avg `0.232` n `26`; metal avg `-0.1567` n `20`; unknown avg `0.6645` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1507`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1357`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0905`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `666`, weak_sample_signal
