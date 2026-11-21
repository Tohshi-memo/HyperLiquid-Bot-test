# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T08:37:29.826798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6747` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4773` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0155` n `13`; crypto_alt avg `-0.4624` n `239`; crypto_major avg `-0.3326` n `8`; equity avg `-0.0342` n `166`; fx avg `-0.0077` n `6`; index avg `-0.0065` n `27`; metal avg `0.0046` n `20`; unknown avg `158.3375` n `1262`
- 1h: commodity avg `-0.0037` n `13`; crypto_alt avg `-1.1518` n `239`; crypto_major avg `-1.5055` n `8`; equity avg `-0.263` n `166`; fx avg `0.008` n `6`; index avg `-0.0282` n `27`; metal avg `-0.0346` n `20`; unknown avg `161.7765` n `1236`
- 4h: commodity avg `-0.0126` n `13`; crypto_alt avg `0.6267` n `239`; crypto_major avg `1.7916` n `8`; equity avg `0.84` n `166`; fx avg `-0.0935` n `6`; index avg `0.078` n `27`; metal avg `0.1169` n `20`; unknown avg `207.8788` n `1204`
- 24h: commodity avg `0.6677` n `13`; crypto_alt avg `-7.0235` n `239`; crypto_major avg `-7.982` n `8`; equity avg `-5.4489` n `166`; fx avg `-0.1152` n `6`; index avg `-0.6136` n `27`; metal avg `-0.5854` n `20`; unknown avg `188.0014` n `1141`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
