# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T05:37:28.925021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.0076` n `234`; crypto_major avg `0.0454` n `8`; equity avg `-0.1054` n `140`; fx avg `0.0171` n `6`; index avg `-0.0024` n `26`; metal avg `-0.1256` n `20`; unknown avg `40.6473` n `944`
- 1h: commodity avg `0.0568` n `12`; crypto_alt avg `-0.463` n `234`; crypto_major avg `-0.3901` n `8`; equity avg `-0.4442` n `140`; fx avg `0.0038` n `6`; index avg `-0.056` n `26`; metal avg `-0.1592` n `20`; unknown avg `47.4459` n `942`
- 4h: commodity avg `0.1451` n `12`; crypto_alt avg `-0.8395` n `234`; crypto_major avg `-0.6478` n `8`; equity avg `-0.8437` n `140`; fx avg `-0.0345` n `6`; index avg `-0.1178` n `26`; metal avg `-0.2676` n `20`; unknown avg `67.7869` n `936`
- 24h: commodity avg `-0.1448` n `12`; crypto_alt avg `2.226` n `234`; crypto_major avg `3.6144` n `8`; equity avg `1.5038` n `140`; fx avg `-0.2558` n `6`; index avg `0.3617` n `26`; metal avg `-0.1699` n `20`; unknown avg `8.1578` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
