# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T21:37:34.418247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.2631` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0381` n `13`; crypto_alt avg `-1.757` n `236`; crypto_major avg `-1.343` n `8`; equity avg `-1.3714` n `151`; fx avg `0.0007` n `6`; index avg `-0.1556` n `26`; metal avg `-0.1162` n `20`; unknown avg `1.371` n `1193`
- 1h: commodity avg `0.0598` n `13`; crypto_alt avg `-1.9375` n `236`; crypto_major avg `-1.4376` n `8`; equity avg `-1.6373` n `151`; fx avg `-0.0025` n `6`; index avg `-0.1745` n `26`; metal avg `-0.1195` n `20`; unknown avg `0.7383` n `1185`
- 4h: commodity avg `0.0126` n `13`; crypto_alt avg `-0.9755` n `236`; crypto_major avg `-0.8315` n `8`; equity avg `-1.4919` n `151`; fx avg `-0.006` n `6`; index avg `-0.1541` n `26`; metal avg `-0.0976` n `20`; unknown avg `0.7153` n `1131`
- 24h: commodity avg `0.0211` n `13`; crypto_alt avg `-3.1382` n `236`; crypto_major avg `-1.8077` n `8`; equity avg `-1.8303` n `151`; fx avg `-0.0289` n `6`; index avg `-0.2078` n `26`; metal avg `-0.1687` n `20`; unknown avg `4.9611` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1686`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1393`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0723`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
