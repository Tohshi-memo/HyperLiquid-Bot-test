# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T22:22:22.945603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `12`; crypto_alt avg `0.192` n `230`; crypto_major avg `0.0495` n `8`; equity avg `0.0069` n `114`; fx avg `0.0226` n `6`; index avg `0.0072` n `25`; metal avg `0.0272` n `20`; unknown avg `0.0086` n `791`
- 1h: commodity avg `-0.0868` n `12`; crypto_alt avg `-0.3836` n `230`; crypto_major avg `-0.3272` n `8`; equity avg `-0.0148` n `114`; fx avg `-0.0123` n `6`; index avg `0.024` n `25`; metal avg `-0.0243` n `20`; unknown avg `-0.0638` n `791`
- 4h: commodity avg `-0.0752` n `12`; crypto_alt avg `-0.6812` n `230`; crypto_major avg `-0.4436` n `8`; equity avg `0.0071` n `114`; fx avg `0.008` n `6`; index avg `0.0372` n `25`; metal avg `-0.0519` n `20`; unknown avg `0.0653` n `791`
- 24h: commodity avg `-0.0103` n `12`; crypto_alt avg `-1.0427` n `230`; crypto_major avg `-0.5443` n `8`; equity avg `0.2861` n `114`; fx avg `-0.0071` n `6`; index avg `0.0633` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0217` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
