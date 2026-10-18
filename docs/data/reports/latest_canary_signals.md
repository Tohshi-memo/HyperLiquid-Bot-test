# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T17:22:27.545558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1858` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `-0.0806` n `237`; crypto_major avg `0.0193` n `8`; equity avg `-0.0661` n `151`; fx avg `0.01` n `6`; index avg `-0.0079` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.0465` n `1194`
- 1h: commodity avg `0.0078` n `13`; crypto_alt avg `-0.1262` n `237`; crypto_major avg `0.1382` n `8`; equity avg `-0.1093` n `151`; fx avg `0.0093` n `6`; index avg `-0.0001` n `26`; metal avg `0.0124` n `20`; unknown avg `-0.3381` n `1192`
- 4h: commodity avg `0.0423` n `13`; crypto_alt avg `-1.6865` n `237`; crypto_major avg `-1.275` n `8`; equity avg `-0.5001` n `151`; fx avg `0.0111` n `6`; index avg `-0.0892` n `26`; metal avg `-0.0449` n `20`; unknown avg `-0.252` n `1159`
- 24h: commodity avg `0.0317` n `13`; crypto_alt avg `-2.583` n `236`; crypto_major avg `-0.9275` n `8`; equity avg `-0.8432` n `151`; fx avg `-0.0063` n `6`; index avg `-0.0956` n `26`; metal avg `-0.0273` n `20`; unknown avg `0.526` n `1017`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1406`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1288`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
