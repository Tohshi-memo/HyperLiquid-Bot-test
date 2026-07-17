# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T03:52:29.156741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `-0.1677` n `230`; crypto_major avg `-0.1787` n `8`; equity avg `-0.1682` n `96`; fx avg `-0.0017` n `6`; index avg `-0.0398` n `25`; metal avg `-0.0345` n `20`; unknown avg `-0.054` n `768`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `0.5789` n `230`; crypto_major avg `0.2981` n `8`; equity avg `0.3128` n `94`; fx avg `0.0036` n `6`; index avg `-0.0071` n `25`; metal avg `0.1365` n `20`; unknown avg `0.0616` n `768`
- 4h: commodity avg `-0.0568` n `12`; crypto_alt avg `-0.0037` n `230`; crypto_major avg `-0.2244` n `8`; equity avg `-1.1954` n `94`; fx avg `-0.0051` n `6`; index avg `-0.2365` n `25`; metal avg `-0.0586` n `20`; unknown avg `-0.2341` n `768`
- 24h: commodity avg `-0.0839` n `12`; crypto_alt avg `-1.7442` n `230`; crypto_major avg `-2.6925` n `8`; equity avg `-5.2438` n `94`; fx avg `-0.1301` n `6`; index avg `-0.6997` n `25`; metal avg `-0.7836` n `20`; unknown avg `-0.3125` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
