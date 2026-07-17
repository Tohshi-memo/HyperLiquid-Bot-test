# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T07:22:30.220196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0104` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.055` n `12`; crypto_alt avg `-0.2815` n `230`; crypto_major avg `-0.2268` n `8`; equity avg `-0.0456` n `96`; fx avg `0.0022` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0437` n `20`; unknown avg `-0.0678` n `768`
- 1h: commodity avg `0.1645` n `12`; crypto_alt avg `-0.2869` n `230`; crypto_major avg `-0.1261` n `8`; equity avg `-0.2609` n `96`; fx avg `-0.0161` n `6`; index avg `-0.0403` n `25`; metal avg `-0.1739` n `20`; unknown avg `-0.0406` n `768`
- 4h: commodity avg `-0.0365` n `12`; crypto_alt avg `-1.0273` n `230`; crypto_major avg `-1.209` n `8`; equity avg `-1.075` n `95`; fx avg `-0.0086` n `6`; index avg `-0.1986` n `25`; metal avg `-0.2152` n `20`; unknown avg `-0.1844` n `736`
- 24h: commodity avg `-0.0385` n `12`; crypto_alt avg `-2.425` n `230`; crypto_major avg `-3.9105` n `8`; equity avg `-5.6912` n `94`; fx avg `-0.0643` n `6`; index avg `-0.7736` n `25`; metal avg `-0.7833` n `20`; unknown avg `-0.6452` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
