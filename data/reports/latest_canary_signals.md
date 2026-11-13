# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T17:52:26.062328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0525` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0244` n `13`; crypto_alt avg `0.0325` n `239`; crypto_major avg `0.0205` n `8`; equity avg `-0.0143` n `162`; fx avg `-0.0007` n `6`; index avg `-0.0045` n `27`; metal avg `0.0112` n `20`; unknown avg `0.3684` n `1262`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `0.2861` n `239`; crypto_major avg `0.5246` n `8`; equity avg `0.6475` n `162`; fx avg `-0.013` n `6`; index avg `0.079` n `27`; metal avg `0.0847` n `20`; unknown avg `0.6029` n `1260`
- 4h: commodity avg `-0.4179` n `13`; crypto_alt avg `-1.1592` n `239`; crypto_major avg `-1.2866` n `8`; equity avg `-2.4453` n `162`; fx avg `-0.0783` n `6`; index avg `-0.2341` n `27`; metal avg `-0.1553` n `20`; unknown avg `7.0647` n `1248`
- 24h: commodity avg `-0.0193` n `13`; crypto_alt avg `0.1005` n `239`; crypto_major avg `-1.6594` n `8`; equity avg `-3.4341` n `162`; fx avg `-0.0138` n `6`; index avg `-0.3096` n `27`; metal avg `-0.1752` n `20`; unknown avg `1.4823` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
