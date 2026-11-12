# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T01:22:30.922331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.607` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4375` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.2024` n `239`; crypto_major avg `-0.2488` n `8`; equity avg `0.0985` n `161`; fx avg `0.0219` n `6`; index avg `-0.0051` n `27`; metal avg `-0.0511` n `20`; unknown avg `1.5665` n `1262`
- 1h: commodity avg `-0.0527` n `13`; crypto_alt avg `-0.7284` n `239`; crypto_major avg `-0.5711` n `8`; equity avg `-0.235` n `161`; fx avg `0.0573` n `6`; index avg `-0.0353` n `27`; metal avg `0.1194` n `20`; unknown avg `22.025` n `1256`
- 4h: commodity avg `-0.0817` n `13`; crypto_alt avg `-1.672` n `239`; crypto_major avg `-1.581` n `8`; equity avg `-1.605` n `161`; fx avg `-0.028` n `6`; index avg `-0.1435` n `27`; metal avg `0.026` n `20`; unknown avg `3.8157` n `1242`
- 24h: commodity avg `0.174` n `13`; crypto_alt avg `-1.6007` n `239`; crypto_major avg `-0.2614` n `8`; equity avg `1.3955` n `161`; fx avg `-0.1496` n `6`; index avg `0.1344` n `27`; metal avg `-0.1614` n `20`; unknown avg `4.2754` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
