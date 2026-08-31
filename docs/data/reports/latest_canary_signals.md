# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T04:37:31.568777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `-0.0109` n `232`; crypto_major avg `0.1167` n `8`; equity avg `0.072` n `128`; fx avg `0.0004` n `6`; index avg `0.0356` n `26`; metal avg `0.0303` n `20`; unknown avg `0.1692` n `793`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `-0.3403` n `231`; crypto_major avg `-0.2888` n `8`; equity avg `0.0338` n `128`; fx avg `-0.001` n `6`; index avg `0.0368` n `26`; metal avg `0.0381` n `20`; unknown avg `0.3377` n `791`
- 4h: commodity avg `0.3166` n `12`; crypto_alt avg `-0.0022` n `231`; crypto_major avg `-0.675` n `8`; equity avg `-0.2728` n `128`; fx avg `-0.0918` n `6`; index avg `0.0234` n `26`; metal avg `-0.3461` n `20`; unknown avg `-0.5047` n `779`
- 24h: commodity avg `0.399` n `12`; crypto_alt avg `-0.3966` n `231`; crypto_major avg `-2.0927` n `8`; equity avg `-1.1018` n `128`; fx avg `-0.0504` n `6`; index avg `-0.1739` n `26`; metal avg `-0.3637` n `20`; unknown avg `-0.4521` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
