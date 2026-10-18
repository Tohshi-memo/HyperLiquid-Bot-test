# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T22:07:23.926697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2444` n `13`; crypto_alt avg `0.9869` n `237`; crypto_major avg `0.9185` n `8`; equity avg `0.5806` n `151`; fx avg `0.0338` n `6`; index avg `0.1953` n `26`; metal avg `0.1714` n `20`; unknown avg `1.4769` n `1190`
- 1h: commodity avg `-0.2848` n `13`; crypto_alt avg `1.7478` n `237`; crypto_major avg `1.5501` n `8`; equity avg `1.0781` n `151`; fx avg `0.0364` n `6`; index avg `0.2616` n `26`; metal avg `0.1941` n `20`; unknown avg `2.3995` n `1118`
- 4h: commodity avg `-0.248` n `13`; crypto_alt avg `0.1705` n `237`; crypto_major avg `0.7855` n `8`; equity avg `0.86` n `151`; fx avg `-0.0141` n `6`; index avg `0.2309` n `26`; metal avg `0.1438` n `20`; unknown avg `6.9946` n `1094`
- 24h: commodity avg `-0.2452` n `13`; crypto_alt avg `-2.2271` n `236`; crypto_major avg `0.2255` n `8`; equity avg `0.8152` n `151`; fx avg `-0.0085` n `6`; index avg `0.228` n `26`; metal avg `0.1773` n `20`; unknown avg `1.7169` n `969`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2031`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1418`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.135`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0777`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `666`, weak_sample_signal
