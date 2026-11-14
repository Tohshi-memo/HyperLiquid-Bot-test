# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T19:52:26.330683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2219` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `-0.2291` n `239`; crypto_major avg `0.0256` n `8`; equity avg `0.0498` n `162`; fx avg `-0.008` n `6`; index avg `0.0101` n `27`; metal avg `0.015` n `20`; unknown avg `4.4198` n `1262`
- 1h: commodity avg `0.0135` n `13`; crypto_alt avg `-0.3377` n `239`; crypto_major avg `0.0495` n `8`; equity avg `0.0563` n `162`; fx avg `0.0118` n `6`; index avg `0.0075` n `27`; metal avg `0.0085` n `20`; unknown avg `2.6571` n `1260`
- 4h: commodity avg `-0.0215` n `13`; crypto_alt avg `-2.1264` n `239`; crypto_major avg `-1.2518` n `8`; equity avg `-0.3211` n `162`; fx avg `0.004` n `6`; index avg `-0.0299` n `27`; metal avg `0.0291` n `20`; unknown avg `0.2289` n `1254`
- 24h: commodity avg `0.0027` n `13`; crypto_alt avg `-7.6603` n `239`; crypto_major avg `-6.8487` n `8`; equity avg `-1.7772` n `162`; fx avg `-0.0211` n `6`; index avg `-0.1416` n `27`; metal avg `-0.2153` n `20`; unknown avg `1.0587` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
