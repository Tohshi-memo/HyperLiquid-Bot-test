# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T21:07:30.445014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.1081` n `230`; crypto_major avg `-0.0896` n `8`; equity avg `-0.0094` n `100`; fx avg `-0.0042` n `6`; index avg `0.0043` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.0143` n `774`
- 1h: commodity avg `0.1409` n `12`; crypto_alt avg `-0.2155` n `230`; crypto_major avg `-0.1583` n `8`; equity avg `0.0393` n `100`; fx avg `-0.0181` n `6`; index avg `0.009` n `25`; metal avg `0.005` n `20`; unknown avg `0.0583` n `774`
- 4h: commodity avg `0.3779` n `12`; crypto_alt avg `-0.1039` n `230`; crypto_major avg `0.0251` n `8`; equity avg `-0.7372` n `100`; fx avg `-0.0284` n `6`; index avg `-0.1315` n `25`; metal avg `-0.1134` n `20`; unknown avg `-0.0245` n `773`
- 24h: commodity avg `-0.3224` n `12`; crypto_alt avg `-1.3647` n `230`; crypto_major avg `-1.2096` n `8`; equity avg `-3.5606` n `100`; fx avg `-0.1699` n `6`; index avg `-0.5078` n `25`; metal avg `-0.0541` n `20`; unknown avg `13.7216` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1262`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1227`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1095`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `666`, weak_sample_signal
