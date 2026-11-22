# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T04:52:31.410169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.57` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.2528` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `-0.1903` n `239`; crypto_major avg `-0.1453` n `8`; equity avg `-0.0729` n `166`; fx avg `0.0057` n `6`; index avg `-0.0055` n `27`; metal avg `-0.0121` n `20`; unknown avg `0.1101` n `1263`
- 1h: commodity avg `0.0023` n `13`; crypto_alt avg `0.1535` n `239`; crypto_major avg `0.0292` n `8`; equity avg `-0.0634` n `166`; fx avg `-0.0125` n `6`; index avg `0.0015` n `27`; metal avg `0.0197` n `20`; unknown avg `326.2258` n `1253`
- 4h: commodity avg `-0.0994` n `13`; crypto_alt avg `-0.9046` n `239`; crypto_major avg `-1.3374` n `8`; equity avg `-0.5132` n `166`; fx avg `-0.0086` n `6`; index avg `-0.0846` n `27`; metal avg `-0.1158` n `20`; unknown avg `8.8362` n `1253`
- 24h: commodity avg `-0.0147` n `13`; crypto_alt avg `2.4461` n `239`; crypto_major avg `4.3067` n `8`; equity avg `1.4093` n `166`; fx avg `-0.0287` n `6`; index avg `0.1824` n `27`; metal avg `0.1362` n `20`; unknown avg `650.2511` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
