# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T04:37:29.625958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3855` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `-0.0469` n `229`; crypto_major avg `0.0005` n `8`; equity avg `0.0158` n `91`; fx avg `0.0085` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0162` n `20`; unknown avg `23.5935` n `763`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.2561` n `229`; crypto_major avg `-0.3832` n `8`; equity avg `-0.4232` n `91`; fx avg `0.0063` n `6`; index avg `-0.0818` n `25`; metal avg `-0.0605` n `20`; unknown avg `12.6673` n `763`
- 4h: commodity avg `-0.0692` n `12`; crypto_alt avg `-1.4448` n `229`; crypto_major avg `-1.6666` n `8`; equity avg `-1.1308` n `91`; fx avg `-0.1114` n `6`; index avg `-0.2811` n `25`; metal avg `-0.2407` n `20`; unknown avg `15.5242` n `761`
- 24h: commodity avg `0.2344` n `12`; crypto_alt avg `-0.2744` n `229`; crypto_major avg `-1.1084` n `8`; equity avg `-1.8153` n `90`; fx avg `-0.0023` n `6`; index avg `-0.369` n `25`; metal avg `-0.3218` n `20`; unknown avg `-0.5211` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
