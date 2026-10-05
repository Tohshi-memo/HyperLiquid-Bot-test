# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T22:22:31.538718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.0462` n `235`; crypto_major avg `0.06` n `8`; equity avg `0.0287` n `144`; fx avg `0.0177` n `6`; index avg `0.0021` n `26`; metal avg `0.011` n `20`; unknown avg `-0.0759` n `1079`
- 1h: commodity avg `0.0076` n `13`; crypto_alt avg `0.1635` n `235`; crypto_major avg `0.334` n `8`; equity avg `0.0359` n `144`; fx avg `0.0133` n `6`; index avg `0.0008` n `26`; metal avg `0.026` n `20`; unknown avg `-0.0034` n `1053`
- 4h: commodity avg `-0.057` n `13`; crypto_alt avg `1.0716` n `235`; crypto_major avg `0.8005` n `8`; equity avg `0.1193` n `144`; fx avg `0.0301` n `6`; index avg `0.0177` n `26`; metal avg `0.0424` n `20`; unknown avg `0.0688` n `979`
- 24h: commodity avg `-0.2722` n `13`; crypto_alt avg `0.6789` n `235`; crypto_major avg `0.0659` n `8`; equity avg `0.3044` n `144`; fx avg `-0.0725` n `6`; index avg `0.1317` n `26`; metal avg `0.1318` n `20`; unknown avg `630.3944` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
