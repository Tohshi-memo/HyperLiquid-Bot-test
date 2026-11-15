# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T15:37:32.881253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3113` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.0306` n `239`; crypto_major avg `-0.0076` n `8`; equity avg `0.0642` n `162`; fx avg `0.0013` n `6`; index avg `0.0166` n `27`; metal avg `0.0127` n `20`; unknown avg `0.0977` n `1264`
- 1h: commodity avg `0.0299` n `13`; crypto_alt avg `-0.2837` n `239`; crypto_major avg `-0.3255` n `8`; equity avg `-0.0073` n `162`; fx avg `0.0016` n `6`; index avg `0.0184` n `27`; metal avg `0.0031` n `20`; unknown avg `1.1253` n `1262`
- 4h: commodity avg `-0.0566` n `13`; crypto_alt avg `-1.0393` n `239`; crypto_major avg `-1.307` n `8`; equity avg `-0.2557` n `162`; fx avg `-0.0227` n `6`; index avg `0.0043` n `27`; metal avg `-0.0336` n `20`; unknown avg `0.3991` n `1253`
- 24h: commodity avg `0.0185` n `13`; crypto_alt avg `-2.3082` n `239`; crypto_major avg `-1.6522` n `8`; equity avg `-0.2428` n `162`; fx avg `-0.007` n `6`; index avg `0.0091` n `27`; metal avg `-0.2233` n `20`; unknown avg `0.0799` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
