# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T13:22:26.507668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3977` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2038` n `13`; crypto_alt avg `-0.2708` n `239`; crypto_major avg `-0.356` n `8`; equity avg `-0.1849` n `165`; fx avg `0.0146` n `6`; index avg `-0.0183` n `27`; metal avg `-0.1194` n `20`; unknown avg `0.1704` n `1260`
- 1h: commodity avg `0.1844` n `13`; crypto_alt avg `-0.4615` n `239`; crypto_major avg `-0.3492` n `8`; equity avg `-0.2536` n `165`; fx avg `0.0497` n `6`; index avg `-0.0467` n `27`; metal avg `-0.1268` n `20`; unknown avg `159.2077` n `1258`
- 4h: commodity avg `0.3504` n `13`; crypto_alt avg `-1.5888` n `239`; crypto_major avg `-1.5644` n `8`; equity avg `-1.2047` n `165`; fx avg `0.0727` n `6`; index avg `-0.1667` n `27`; metal avg `-0.1608` n `20`; unknown avg `177.227` n `1250`
- 24h: commodity avg `-0.2271` n `13`; crypto_alt avg `-4.8436` n `239`; crypto_major avg `-4.5104` n `8`; equity avg `-8.5245` n `165`; fx avg `0.0027` n `6`; index avg `-0.8733` n `27`; metal avg `-1.3264` n `20`; unknown avg `25.8298` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
