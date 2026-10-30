# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T09:37:38.114561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2529` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `0.0687` n `238`; crypto_major avg `0.0663` n `8`; equity avg `0.0739` n `156`; fx avg `-0.0056` n `6`; index avg `-0.0187` n `27`; metal avg `0.0105` n `20`; unknown avg `0.2245` n `1261`
- 1h: commodity avg `-0.0355` n `13`; crypto_alt avg `-0.1086` n `238`; crypto_major avg `-0.2657` n `8`; equity avg `0.0293` n `156`; fx avg `0.0265` n `6`; index avg `-0.0069` n `27`; metal avg `0.0973` n `20`; unknown avg `14.5454` n `1255`
- 4h: commodity avg `0.1676` n `13`; crypto_alt avg `-0.4566` n `238`; crypto_major avg `-1.2677` n `8`; equity avg `-0.7205` n `156`; fx avg `0.0233` n `6`; index avg `-0.0148` n `27`; metal avg `-0.2323` n `20`; unknown avg `3.513` n `1172`
- 24h: commodity avg `0.0209` n `13`; crypto_alt avg `-3.4032` n `238`; crypto_major avg `-0.8604` n `8`; equity avg `-3.1919` n `155`; fx avg `0.1387` n `6`; index avg `-0.4018` n `27`; metal avg `-0.528` n `20`; unknown avg `31.1093` n `946`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
