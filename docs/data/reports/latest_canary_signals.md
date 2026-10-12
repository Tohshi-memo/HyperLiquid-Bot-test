# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T07:22:30.362695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `13`; crypto_alt avg `0.0501` n `235`; crypto_major avg `0.0493` n `8`; equity avg `0.0901` n `151`; fx avg `-0.0082` n `6`; index avg `0.0108` n `26`; metal avg `-0.0366` n `20`; unknown avg `0.1042` n `1133`
- 1h: commodity avg `-0.012` n `13`; crypto_alt avg `0.1482` n `235`; crypto_major avg `0.4931` n `8`; equity avg `0.0341` n `151`; fx avg `-0.0251` n `6`; index avg `0.0059` n `26`; metal avg `0.0184` n `20`; unknown avg `-0.0197` n `1131`
- 4h: commodity avg `0.2486` n `13`; crypto_alt avg `0.3228` n `235`; crypto_major avg `0.7099` n `8`; equity avg `-0.3013` n `151`; fx avg `-0.0035` n `6`; index avg `-0.0643` n `26`; metal avg `-0.0873` n `20`; unknown avg `0.1187` n `1043`
- 24h: commodity avg `-0.2944` n `13`; crypto_alt avg `2.5644` n `235`; crypto_major avg `2.0833` n `8`; equity avg `-0.5127` n `151`; fx avg `-0.0814` n `6`; index avg `-0.0509` n `26`; metal avg `0.0565` n `20`; unknown avg `0.3883` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
