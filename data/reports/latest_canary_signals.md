# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T22:07:28.693638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0853` n `12`; crypto_alt avg `-0.1101` n `230`; crypto_major avg `-0.0812` n `8`; equity avg `-0.0337` n `92`; fx avg `0.0031` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0297` n `20`; unknown avg `-0.0366` n `768`
- 1h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.0233` n `230`; crypto_major avg `-0.1157` n `8`; equity avg `-0.0216` n `92`; fx avg `-0.0047` n `6`; index avg `-0.0069` n `25`; metal avg `0.0077` n `20`; unknown avg `2.3424` n `768`
- 4h: commodity avg `0.2095` n `12`; crypto_alt avg `-0.1506` n `230`; crypto_major avg `0.1091` n `8`; equity avg `0.0499` n `92`; fx avg `0.005` n `6`; index avg `-0.0309` n `25`; metal avg `-0.0349` n `20`; unknown avg `-0.1961` n `768`
- 24h: commodity avg `0.3629` n `12`; crypto_alt avg `2.2192` n `230`; crypto_major avg `3.528` n `8`; equity avg `1.3304` n `92`; fx avg `-0.0062` n `6`; index avg `0.3854` n `25`; metal avg `0.5732` n `20`; unknown avg `0.2669` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
