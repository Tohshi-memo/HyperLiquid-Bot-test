# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T16:07:28.486858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.477` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1395` n `13`; crypto_alt avg `-0.1835` n `239`; crypto_major avg `-0.3625` n `8`; equity avg `-0.5621` n `168`; fx avg `-0.005` n `6`; index avg `-0.0687` n `27`; metal avg `-0.2058` n `20`; unknown avg `14.1649` n `1249`
- 1h: commodity avg `-0.2559` n `13`; crypto_alt avg `-0.5101` n `239`; crypto_major avg `-0.3933` n `8`; equity avg `-1.5923` n `168`; fx avg `-0.0133` n `6`; index avg `-0.1741` n `27`; metal avg `-0.5533` n `20`; unknown avg `214.3148` n `1255`
- 4h: commodity avg `0.0689` n `13`; crypto_alt avg `-1.6968` n `239`; crypto_major avg `-1.7001` n `8`; equity avg `-2.639` n `167`; fx avg `0.0538` n `6`; index avg `-0.2231` n `27`; metal avg `-0.6526` n `20`; unknown avg `582.6894` n `1245`
- 24h: commodity avg `0.5147` n `13`; crypto_alt avg `-5.5369` n `239`; crypto_major avg `-5.8564` n `8`; equity avg `-5.594` n `167`; fx avg `0.1724` n `6`; index avg `-0.4642` n `27`; metal avg `-1.3811` n `20`; unknown avg `1.2035` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
