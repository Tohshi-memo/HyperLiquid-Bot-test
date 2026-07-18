# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T02:37:22.939403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0395` n `12`; crypto_alt avg `0.094` n `230`; crypto_major avg `0.0035` n `8`; equity avg `-0.048` n `96`; fx avg `-0.0012` n `6`; index avg `-0.0047` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.02` n `769`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `0.1079` n `230`; crypto_major avg `0.1912` n `8`; equity avg `-0.0393` n `96`; fx avg `-0.0134` n `6`; index avg `0.0207` n `25`; metal avg `-0.0244` n `20`; unknown avg `-0.2688` n `769`
- 4h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.2784` n `230`; crypto_major avg `0.2425` n `8`; equity avg `0.1231` n `96`; fx avg `-0.0029` n `6`; index avg `0.0425` n `25`; metal avg `0.026` n `20`; unknown avg `-0.3614` n `769`
- 24h: commodity avg `0.7583` n `12`; crypto_alt avg `0.2117` n `230`; crypto_major avg `0.144` n `8`; equity avg `0.838` n `94`; fx avg `0.0502` n `6`; index avg `0.0012` n `25`; metal avg `0.2353` n `20`; unknown avg `0.2445` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
