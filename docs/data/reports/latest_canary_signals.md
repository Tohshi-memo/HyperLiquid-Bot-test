# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T23:37:26.338712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0741` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.0208` n `230`; crypto_major avg `0.0187` n `8`; equity avg `-0.2593` n `94`; fx avg `0.0027` n `6`; index avg `-0.0341` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0714` n `768`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.6464` n `230`; crypto_major avg `-0.63` n `8`; equity avg `-0.6886` n `94`; fx avg `0.0182` n `6`; index avg `-0.0508` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.2111` n `768`
- 4h: commodity avg `0.1118` n `12`; crypto_alt avg `-1.0279` n `230`; crypto_major avg `-1.0858` n `8`; equity avg `-0.8563` n `94`; fx avg `0.0014` n `6`; index avg `-0.0117` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.3572` n `768`
- 24h: commodity avg `-0.1555` n `12`; crypto_alt avg `-2.0567` n `230`; crypto_major avg `-2.9875` n `8`; equity avg `-4.5471` n `94`; fx avg `-0.1378` n `6`; index avg `-0.6022` n `25`; metal avg `-0.8551` n `20`; unknown avg `-0.5797` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
