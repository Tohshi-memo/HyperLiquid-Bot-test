# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T10:52:26.436708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0683` n `12`; crypto_alt avg `0.0596` n `230`; crypto_major avg `0.0874` n `8`; equity avg `0.0977` n `113`; fx avg `-0.0027` n `6`; index avg `0.0085` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0707` n `785`
- 1h: commodity avg `-0.2429` n `12`; crypto_alt avg `-0.109` n `230`; crypto_major avg `0.021` n `8`; equity avg `0.2262` n `113`; fx avg `-0.0305` n `6`; index avg `0.0462` n `25`; metal avg `0.034` n `20`; unknown avg `-0.0184` n `785`
- 4h: commodity avg `-0.1637` n `12`; crypto_alt avg `-0.0132` n `230`; crypto_major avg `0.5155` n `8`; equity avg `0.2964` n `113`; fx avg `-0.0458` n `6`; index avg `0.0769` n `25`; metal avg `0.2276` n `20`; unknown avg `0.0668` n `785`
- 24h: commodity avg `0.7223` n `12`; crypto_alt avg `-1.2304` n `230`; crypto_major avg `-0.5284` n `8`; equity avg `-1.0836` n `113`; fx avg `-0.0053` n `6`; index avg `0.0378` n `25`; metal avg `0.4047` n `20`; unknown avg `0.1504` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
