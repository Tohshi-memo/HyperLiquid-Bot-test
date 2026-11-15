# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T08:22:24.481940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3509` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0238` n `13`; crypto_alt avg `-0.0909` n `239`; crypto_major avg `0.2636` n `8`; equity avg `0.0234` n `162`; fx avg `-0.0096` n `6`; index avg `-0.0025` n `27`; metal avg `0.0025` n `20`; unknown avg `0.1477` n `1261`
- 1h: commodity avg `-0.0226` n `13`; crypto_alt avg `-0.6515` n `239`; crypto_major avg `-0.385` n `8`; equity avg `-0.0807` n `162`; fx avg `-0.0078` n `6`; index avg `-0.0033` n `27`; metal avg `-0.014` n `20`; unknown avg `0.461` n `1245`
- 4h: commodity avg `-0.0439` n `13`; crypto_alt avg `-1.1243` n `239`; crypto_major avg `-1.3775` n `8`; equity avg `-0.2795` n `162`; fx avg `-0.0113` n `6`; index avg `-0.0266` n `27`; metal avg `-0.0256` n `20`; unknown avg `0.6596` n `1221`
- 24h: commodity avg `0.0037` n `13`; crypto_alt avg `-5.7299` n `239`; crypto_major avg `-5.0287` n `8`; equity avg `-1.0662` n `162`; fx avg `0.0344` n `6`; index avg `-0.1042` n `27`; metal avg `-0.423` n `20`; unknown avg `46.7313` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
