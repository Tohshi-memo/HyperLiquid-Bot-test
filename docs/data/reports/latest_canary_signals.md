# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T04:22:25.894344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2057` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0665` n `229`; crypto_major avg `-0.1069` n `8`; equity avg `-0.1534` n `91`; fx avg `0.0088` n `6`; index avg `-0.0264` n `25`; metal avg `-0.085` n `20`; unknown avg `0.1094` n `763`
- 1h: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.2249` n `229`; crypto_major avg `-0.4037` n `8`; equity avg `-0.5341` n `91`; fx avg `0.0136` n `6`; index avg `-0.1143` n `25`; metal avg `-0.0691` n `20`; unknown avg `-0.1934` n `763`
- 4h: commodity avg `-0.0596` n `12`; crypto_alt avg `-1.4382` n `229`; crypto_major avg `-1.571` n `8`; equity avg `-1.4108` n `91`; fx avg `-0.1066` n `6`; index avg `-0.3653` n `25`; metal avg `-0.3161` n `20`; unknown avg `1.5553` n `761`
- 24h: commodity avg `0.2399` n `12`; crypto_alt avg `-0.3984` n `229`; crypto_major avg `-1.2026` n `8`; equity avg `-1.6933` n `90`; fx avg `-0.0288` n `6`; index avg `-0.3208` n `25`; metal avg `-0.3042` n `20`; unknown avg `-0.3881` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
