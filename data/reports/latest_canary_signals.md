# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T08:07:33.859314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0324` n `13`; crypto_alt avg `-0.2521` n `239`; crypto_major avg `-0.321` n `8`; equity avg `0.02` n `162`; fx avg `-0.0007` n `6`; index avg `0.0257` n `27`; metal avg `0.036` n `20`; unknown avg `0.9049` n `1219`
- 1h: commodity avg `-0.0556` n `13`; crypto_alt avg `-0.0775` n `239`; crypto_major avg `-0.0868` n `8`; equity avg `0.1134` n `162`; fx avg `-0.0066` n `6`; index avg `0.0353` n `27`; metal avg `-0.0197` n `20`; unknown avg `0.926` n `1215`
- 4h: commodity avg `0.0095` n `13`; crypto_alt avg `-0.4171` n `239`; crypto_major avg `-0.2252` n `8`; equity avg `-0.3702` n `162`; fx avg `-0.023` n `6`; index avg `0.0052` n `27`; metal avg `-0.0492` n `20`; unknown avg `0.1345` n `1077`
- 24h: commodity avg `-0.2414` n `13`; crypto_alt avg `0.3583` n `239`; crypto_major avg `1.2787` n `8`; equity avg `-0.1218` n `162`; fx avg `-0.0661` n `6`; index avg `0.0221` n `27`; metal avg `0.0864` n `20`; unknown avg `0.4838` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
