# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T12:07:24.853453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0302` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0617` n `13`; crypto_alt avg `0.1438` n `239`; crypto_major avg `0.116` n `8`; equity avg `-0.2094` n `162`; fx avg `-0.0062` n `6`; index avg `-0.0114` n `27`; metal avg `0.0012` n `20`; unknown avg `20.8714` n `1251`
- 1h: commodity avg `-0.0083` n `13`; crypto_alt avg `-0.7041` n `239`; crypto_major avg `-0.9776` n `8`; equity avg `-0.408` n `162`; fx avg `-0.0092` n `6`; index avg `-0.0197` n `27`; metal avg `-0.073` n `20`; unknown avg `19.2413` n `1249`
- 4h: commodity avg `-0.2571` n `13`; crypto_alt avg `-0.6188` n `239`; crypto_major avg `-1.0101` n `8`; equity avg `-0.2338` n `162`; fx avg `-0.0332` n `6`; index avg `0.0201` n `27`; metal avg `-0.2522` n `20`; unknown avg `19.3217` n `1243`
- 24h: commodity avg `-0.2111` n `13`; crypto_alt avg `-2.4305` n `239`; crypto_major avg `-1.7229` n `8`; equity avg `-1.5614` n `162`; fx avg `-0.0928` n `6`; index avg `-0.1007` n `27`; metal avg `-0.8692` n `20`; unknown avg `0.6728` n `1140`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
