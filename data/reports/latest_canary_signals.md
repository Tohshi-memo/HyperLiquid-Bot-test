# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T10:22:24.866858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1065` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.0889` n `233`; crypto_major avg `-0.0688` n `8`; equity avg `-0.0601` n `136`; fx avg `-0.0011` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0042` n `20`; unknown avg `0.0274` n `838`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.3803` n `233`; crypto_major avg `-0.6645` n `8`; equity avg `-0.5422` n `136`; fx avg `0.0069` n `6`; index avg `-0.0932` n `27`; metal avg `-0.0289` n `20`; unknown avg `0.023` n `830`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.9028` n `233`; crypto_major avg `-1.2612` n `8`; equity avg `-1.0004` n `136`; fx avg `0.0053` n `6`; index avg `-0.1547` n `26`; metal avg `-0.0541` n `20`; unknown avg `0.1427` n `830`
- 24h: commodity avg `0.0906` n `12`; crypto_alt avg `-0.5296` n `233`; crypto_major avg `-1.772` n `8`; equity avg `-1.6557` n `136`; fx avg `-0.0002` n `6`; index avg `-0.2637` n `26`; metal avg `-0.0316` n `20`; unknown avg `0.0717` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
