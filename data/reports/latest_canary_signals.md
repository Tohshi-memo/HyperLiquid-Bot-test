# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T16:37:29.477687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.0185` n `229`; crypto_major avg `-0.0112` n `8`; equity avg `-0.0197` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0196` n `765`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `0.254` n `229`; crypto_major avg `-0.0388` n `8`; equity avg `-0.0039` n `88`; fx avg `-0.0056` n `6`; index avg `-0.0033` n `25`; metal avg `0.0057` n `20`; unknown avg `0.1763` n `765`
- 4h: commodity avg `-0.0568` n `12`; crypto_alt avg `0.8561` n `229`; crypto_major avg `0.8954` n `8`; equity avg `0.0403` n `88`; fx avg `0.0177` n `6`; index avg `-0.0125` n `25`; metal avg `0.0322` n `20`; unknown avg `0.3146` n `759`
- 24h: commodity avg `0.0297` n `12`; crypto_alt avg `1.5284` n `229`; crypto_major avg `1.9823` n `8`; equity avg `0.2496` n `88`; fx avg `-0.0229` n `6`; index avg `-0.0482` n `25`; metal avg `0.0721` n `20`; unknown avg `1.8646` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
