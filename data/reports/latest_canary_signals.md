# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T01:52:30.340436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1276` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.4602` n `230`; crypto_major avg `-0.6272` n `8`; equity avg `-0.3202` n `94`; fx avg `-0.0097` n `6`; index avg `-0.0499` n `25`; metal avg `-0.1192` n `20`; unknown avg `0.3732` n `768`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.4766` n `230`; crypto_major avg `-0.6118` n `8`; equity avg `-0.6842` n `94`; fx avg `0.0037` n `6`; index avg `-0.1241` n `25`; metal avg `-0.1249` n `20`; unknown avg `0.161` n `768`
- 4h: commodity avg `0.0359` n `12`; crypto_alt avg `-1.3591` n `230`; crypto_major avg `-1.3984` n `8`; equity avg `-1.767` n `94`; fx avg `-0.0195` n `6`; index avg `-0.2708` n `25`; metal avg `-0.152` n `20`; unknown avg `-0.3515` n `768`
- 24h: commodity avg `-0.1034` n `12`; crypto_alt avg `-2.1888` n `230`; crypto_major avg `-3.1293` n `8`; equity avg `-4.9263` n `94`; fx avg `-0.1856` n `6`; index avg `-0.6204` n `25`; metal avg `-0.7577` n `20`; unknown avg `-0.7109` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
