# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T06:37:25.580551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0647` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.3105` n `230`; crypto_major avg `-0.4719` n `8`; equity avg `-0.1169` n `98`; fx avg `-0.0005` n `6`; index avg `-0.0345` n `25`; metal avg `-0.0319` n `20`; unknown avg `0.0243` n `769`
- 1h: commodity avg `0.0878` n `12`; crypto_alt avg `-0.2157` n `230`; crypto_major avg `-0.4364` n `8`; equity avg `-0.2733` n `98`; fx avg `-0.0265` n `6`; index avg `-0.0348` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.0216` n `753`
- 4h: commodity avg `0.0751` n `12`; crypto_alt avg `-1.0955` n `230`; crypto_major avg `-1.1523` n `8`; equity avg `-0.2426` n `98`; fx avg `-0.0292` n `6`; index avg `-0.0876` n `25`; metal avg `-0.0981` n `20`; unknown avg `-0.3171` n `753`
- 24h: commodity avg `0.0589` n `12`; crypto_alt avg `-0.9855` n `230`; crypto_major avg `-1.0689` n `8`; equity avg `-0.2551` n `97`; fx avg `-0.0609` n `6`; index avg `-0.0378` n `25`; metal avg `-0.0589` n `20`; unknown avg `-0.1903` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0937`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0909`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
