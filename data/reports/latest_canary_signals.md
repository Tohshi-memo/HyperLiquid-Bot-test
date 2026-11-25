# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T02:52:25.491781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2634` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.0641` n `239`; crypto_major avg `-0.0447` n `8`; equity avg `-0.3437` n `168`; fx avg `-0.0037` n `6`; index avg `-0.015` n `27`; metal avg `-0.1859` n `20`; unknown avg `-0.2083` n `1265`
- 1h: commodity avg `-0.1121` n `13`; crypto_alt avg `0.1192` n `239`; crypto_major avg `0.1153` n `8`; equity avg `-0.7156` n `168`; fx avg `-0.0068` n `6`; index avg `-0.0613` n `27`; metal avg `-0.1174` n `20`; unknown avg `24.0241` n `1259`
- 4h: commodity avg `-0.1788` n `13`; crypto_alt avg `-0.8806` n `239`; crypto_major avg `-1.457` n `8`; equity avg `-1.9871` n `168`; fx avg `-0.0041` n `6`; index avg `-0.1936` n `27`; metal avg `-0.1092` n `20`; unknown avg `86.1521` n `1205`
- 24h: commodity avg `0.5199` n `13`; crypto_alt avg `-2.9562` n `239`; crypto_major avg `-2.503` n `8`; equity avg `-5.2402` n `167`; fx avg `0.1812` n `6`; index avg `-0.5392` n `27`; metal avg `-0.9867` n `20`; unknown avg `489.5538` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
