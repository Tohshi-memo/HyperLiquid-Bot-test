# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T01:37:30.497532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.043` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.4709` n `233`; crypto_major avg `-0.276` n `8`; equity avg `-0.1693` n `134`; fx avg `0.0078` n `6`; index avg `-0.0194` n `26`; metal avg `-0.0522` n `20`; unknown avg `0.1207` n `797`
- 1h: commodity avg `0.0038` n `12`; crypto_alt avg `-0.7364` n `233`; crypto_major avg `-0.5045` n `8`; equity avg `-0.5178` n `134`; fx avg `0.0254` n `6`; index avg `-0.0922` n `26`; metal avg `-0.0095` n `20`; unknown avg `8.8837` n `795`
- 4h: commodity avg `-0.0361` n `12`; crypto_alt avg `-2.0485` n `233`; crypto_major avg `-1.1299` n `8`; equity avg `-0.7099` n `134`; fx avg `0.0066` n `6`; index avg `-0.0869` n `26`; metal avg `-0.0399` n `20`; unknown avg `0.794` n `729`
- 24h: commodity avg `0.0478` n `12`; crypto_alt avg `-3.7445` n `233`; crypto_major avg `-2.636` n `8`; equity avg `-1.6925` n `134`; fx avg `0.0139` n `6`; index avg `-0.3246` n `26`; metal avg `0.3435` n `20`; unknown avg `1.1605` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
