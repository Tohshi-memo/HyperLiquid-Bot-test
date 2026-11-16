# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T01:37:23.389588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0656` n `13`; crypto_alt avg `-0.0347` n `239`; crypto_major avg `0.0528` n `8`; equity avg `-0.1812` n `162`; fx avg `-0.0048` n `6`; index avg `-0.0126` n `27`; metal avg `-0.1077` n `20`; unknown avg `0.2024` n `1265`
- 1h: commodity avg `-0.0843` n `13`; crypto_alt avg `-0.6264` n `239`; crypto_major avg `-0.548` n `8`; equity avg `-1.2856` n `162`; fx avg `0.0221` n `6`; index avg `-0.1664` n `27`; metal avg `-0.336` n `20`; unknown avg `1.0109` n `1253`
- 4h: commodity avg `-0.323` n `13`; crypto_alt avg `-0.5417` n `239`; crypto_major avg `-0.4992` n `8`; equity avg `-0.5155` n `162`; fx avg `-0.0269` n `6`; index avg `-0.0424` n `27`; metal avg `-0.06` n `20`; unknown avg `0.425` n `1195`
- 24h: commodity avg `-0.3759` n `13`; crypto_alt avg `2.4597` n `239`; crypto_major avg `4.2289` n `8`; equity avg `0.9073` n `162`; fx avg `0.0076` n `6`; index avg `0.0727` n `27`; metal avg `0.2556` n `20`; unknown avg `2.2548` n `1128`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
