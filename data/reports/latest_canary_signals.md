# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T11:52:26.242306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1301` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.1203` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0247` n `13`; crypto_alt avg `-0.2391` n `239`; crypto_major avg `-0.323` n `8`; equity avg `0.0467` n `162`; fx avg `-0.0053` n `6`; index avg `0.003` n `27`; metal avg `-0.0098` n `20`; unknown avg `0.3014` n `1261`
- 1h: commodity avg `0.033` n `13`; crypto_alt avg `-0.8431` n `239`; crypto_major avg `-1.1462` n `8`; equity avg `-0.3124` n `162`; fx avg `-0.0007` n `6`; index avg `-0.0161` n `27`; metal avg `-0.0971` n `20`; unknown avg `0.298` n `1255`
- 4h: commodity avg `-0.1349` n `13`; crypto_alt avg `-0.7152` n `239`; crypto_major avg `-1.0713` n `8`; equity avg `0.1453` n `162`; fx avg `-0.0103` n `6`; index avg `0.049` n `27`; metal avg `-0.2336` n `20`; unknown avg `0.0185` n `1233`
- 24h: commodity avg `-0.0405` n `13`; crypto_alt avg `-2.7277` n `239`; crypto_major avg `-2.1089` n `8`; equity avg `-1.2182` n `162`; fx avg `-0.0863` n `6`; index avg `-0.0796` n `27`; metal avg `-0.8762` n `20`; unknown avg `-0.1124` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
