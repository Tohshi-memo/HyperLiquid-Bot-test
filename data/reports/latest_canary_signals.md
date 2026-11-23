# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T21:52:31.486029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3736` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0309` n `13`; crypto_alt avg `-0.2043` n `239`; crypto_major avg `-0.1922` n `8`; equity avg `0.0091` n `166`; fx avg `-0.0048` n `6`; index avg `0.0059` n `27`; metal avg `-0.0184` n `20`; unknown avg `0.4211` n `1266`
- 1h: commodity avg `0.0846` n `13`; crypto_alt avg `-0.0178` n `239`; crypto_major avg `0.0469` n `8`; equity avg `0.3777` n `166`; fx avg `-0.0079` n `6`; index avg `0.0453` n `27`; metal avg `-0.011` n `20`; unknown avg `-0.1149` n `1234`
- 4h: commodity avg `-0.1569` n `13`; crypto_alt avg `-1.4621` n `239`; crypto_major avg `-1.3481` n `8`; equity avg `0.0047` n `166`; fx avg `-0.009` n `6`; index avg `0.0255` n `27`; metal avg `-0.1537` n `20`; unknown avg `326.8593` n `1228`
- 24h: commodity avg `-1.3976` n `13`; crypto_alt avg `0.8256` n `239`; crypto_major avg `1.1327` n `8`; equity avg `5.8439` n `166`; fx avg `-0.1441` n `6`; index avg `0.549` n `27`; metal avg `0.5485` n `20`; unknown avg `242.3274` n `1050`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
