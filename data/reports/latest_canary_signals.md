# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T17:52:27.820456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.1029` n `234`; crypto_major avg `0.1042` n `8`; equity avg `0.0244` n `140`; fx avg `-0.0202` n `6`; index avg `0.0004` n `26`; metal avg `0.0078` n `20`; unknown avg `0.1931` n `943`
- 1h: commodity avg `0.0523` n `12`; crypto_alt avg `-0.25` n `234`; crypto_major avg `-0.2241` n `8`; equity avg `0.0017` n `140`; fx avg `-0.0027` n `6`; index avg `-0.0036` n `26`; metal avg `0.0033` n `20`; unknown avg `18.3116` n `907`
- 4h: commodity avg `-0.1032` n `12`; crypto_alt avg `0.2634` n `234`; crypto_major avg `0.0759` n `8`; equity avg `0.0162` n `140`; fx avg `-0.0132` n `6`; index avg `0.0125` n `26`; metal avg `0.0041` n `20`; unknown avg `6.2489` n `882`
- 24h: commodity avg `-0.055` n `12`; crypto_alt avg `2.5475` n `234`; crypto_major avg `1.1403` n `8`; equity avg `0.4743` n `140`; fx avg `0.0153` n `6`; index avg `0.1319` n `26`; metal avg `-0.12` n `20`; unknown avg `3.9721` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
