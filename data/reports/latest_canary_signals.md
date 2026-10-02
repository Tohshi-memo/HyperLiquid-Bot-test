# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T22:07:29.222425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2428` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.001` n `13`; crypto_alt avg `0.1638` n `235`; crypto_major avg `0.0279` n `8`; equity avg `-0.0069` n `143`; fx avg `0.0` n `6`; index avg `-0.0796` n `26`; metal avg `0.015` n `20`; unknown avg `-0.122` n `974`
- 1h: commodity avg `0.1231` n `13`; crypto_alt avg `0.4739` n `235`; crypto_major avg `0.1067` n `8`; equity avg `-0.025` n `143`; fx avg `-0.0006` n `6`; index avg `-0.0713` n `26`; metal avg `0.021` n `20`; unknown avg `-0.1006` n `966`
- 4h: commodity avg `0.2243` n `13`; crypto_alt avg `-1.8559` n `235`; crypto_major avg `-1.2856` n `8`; equity avg `0.0628` n `143`; fx avg `-0.0221` n `6`; index avg `-0.0428` n `26`; metal avg `0.1171` n `20`; unknown avg `-0.4449` n `906`
- 24h: commodity avg `0.0532` n `13`; crypto_alt avg `-1.1502` n `235`; crypto_major avg `-0.8553` n `8`; equity avg `0.7239` n `142`; fx avg `-0.1576` n `6`; index avg `0.2249` n `26`; metal avg `-0.217` n `20`; unknown avg `-0.4599` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
