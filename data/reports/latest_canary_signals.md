# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T02:22:29.503583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1459` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0598` n `13`; crypto_alt avg `-0.0736` n `239`; crypto_major avg `-0.0088` n `8`; equity avg `-0.3328` n `168`; fx avg `0.008` n `6`; index avg `-0.0467` n `27`; metal avg `0.0694` n `20`; unknown avg `26.1025` n `1263`
- 1h: commodity avg `-0.1305` n `13`; crypto_alt avg `-0.3903` n `239`; crypto_major avg `-0.6841` n `8`; equity avg `-0.9383` n `168`; fx avg `0.0221` n `6`; index avg `-0.1316` n `27`; metal avg `0.3195` n `20`; unknown avg `25.2551` n `1259`
- 4h: commodity avg `-0.1428` n `13`; crypto_alt avg `-0.6373` n `239`; crypto_major avg `-1.3347` n `8`; equity avg `-1.5967` n `168`; fx avg `0.0276` n `6`; index avg `-0.1888` n `27`; metal avg `0.0888` n `20`; unknown avg `171.9364` n `1173`
- 24h: commodity avg `0.5178` n `13`; crypto_alt avg `-3.4637` n `239`; crypto_major avg `-3.1903` n `8`; equity avg `-5.1447` n `167`; fx avg `0.1891` n `6`; index avg `-0.5472` n `27`; metal avg `-0.9923` n `20`; unknown avg `484.1588` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
