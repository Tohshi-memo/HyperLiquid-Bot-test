# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T13:22:34.028890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `0.0746` n `239`; crypto_major avg `0.0061` n `8`; equity avg `-0.0002` n `162`; fx avg `-0.0056` n `6`; index avg `-0.0143` n `27`; metal avg `-0.0659` n `20`; unknown avg `1.608` n `1260`
- 1h: commodity avg `-0.1017` n `13`; crypto_alt avg `-0.0414` n `239`; crypto_major avg `-0.0556` n `8`; equity avg `-0.3194` n `162`; fx avg `0.0086` n `6`; index avg `-0.0333` n `27`; metal avg `-0.0613` n `20`; unknown avg `160.2` n `1260`
- 4h: commodity avg `-0.0739` n `13`; crypto_alt avg `0.6429` n `239`; crypto_major avg `0.9146` n `8`; equity avg `0.2366` n `162`; fx avg `-0.011` n `6`; index avg `0.0229` n `27`; metal avg `0.0221` n `20`; unknown avg `43.7752` n `1200`
- 24h: commodity avg `0.3737` n `13`; crypto_alt avg `0.7794` n `239`; crypto_major avg `-0.8844` n `8`; equity avg `0.26` n `162`; fx avg `-0.0199` n `6`; index avg `0.1111` n `27`; metal avg `-0.2155` n `20`; unknown avg `2.5982` n `1075`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
