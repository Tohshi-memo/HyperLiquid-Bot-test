# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T02:37:29.161312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.4828` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0439` n `13`; crypto_alt avg `0.0364` n `237`; crypto_major avg `0.0164` n `8`; equity avg `0.0324` n `151`; fx avg `0.0074` n `6`; index avg `0.0081` n `26`; metal avg `0.0324` n `20`; unknown avg `-0.3009` n `1201`
- 1h: commodity avg `0.0308` n `13`; crypto_alt avg `-1.2851` n `237`; crypto_major avg `-0.9668` n `8`; equity avg `-0.563` n `151`; fx avg `-0.0386` n `6`; index avg `-0.0458` n `26`; metal avg `-0.0933` n `20`; unknown avg `10.1876` n `1199`
- 4h: commodity avg `0.1378` n `13`; crypto_alt avg `-1.7442` n `237`; crypto_major avg `-1.5972` n `8`; equity avg `-1.0499` n `151`; fx avg `-0.0349` n `6`; index avg `-0.1144` n `26`; metal avg `-0.3135` n `20`; unknown avg `8.2613` n `1193`
- 24h: commodity avg `-0.5732` n `13`; crypto_alt avg `-0.3998` n `237`; crypto_major avg `-0.517` n `8`; equity avg `-1.8216` n `151`; fx avg `-0.0498` n `6`; index avg `-0.2509` n `26`; metal avg `-0.3655` n `20`; unknown avg `118.806` n `946`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
