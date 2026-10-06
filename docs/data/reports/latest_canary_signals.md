# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T08:37:32.063012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1438` n `13`; crypto_alt avg `0.0385` n `235`; crypto_major avg `0.014` n `8`; equity avg `-0.0447` n `149`; fx avg `0.0065` n `6`; index avg `-0.0033` n `26`; metal avg `0.049` n `20`; unknown avg `-0.072` n `1074`
- 1h: commodity avg `-0.1264` n `13`; crypto_alt avg `0.3432` n `235`; crypto_major avg `0.3222` n `8`; equity avg `0.0221` n `149`; fx avg `-0.0119` n `6`; index avg `0.0156` n `26`; metal avg `0.1234` n `20`; unknown avg `0.1911` n `1056`
- 4h: commodity avg `-0.33` n `13`; crypto_alt avg `0.4895` n `235`; crypto_major avg `0.0633` n `8`; equity avg `0.1332` n `149`; fx avg `-0.007` n `6`; index avg `0.0527` n `26`; metal avg `0.1233` n `20`; unknown avg `-0.1315` n `976`
- 24h: commodity avg `-0.6622` n `13`; crypto_alt avg `-0.8866` n `235`; crypto_major avg `-0.8182` n `8`; equity avg `0.2793` n `149`; fx avg `0.0071` n `6`; index avg `0.1902` n `26`; metal avg `-0.1195` n `20`; unknown avg `0.0451` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
