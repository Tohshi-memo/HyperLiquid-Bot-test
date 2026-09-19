# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T11:37:25.639490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.33` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0306` n `234`; crypto_major avg `-0.046` n `8`; equity avg `0.0053` n `140`; fx avg `0.0` n `6`; index avg `-0.0009` n `26`; metal avg `0.0108` n `20`; unknown avg `0.1135` n `942`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `0.2361` n `234`; crypto_major avg `0.132` n `8`; equity avg `0.0082` n `140`; fx avg `-0.0062` n `6`; index avg `-0.0065` n `26`; metal avg `0.0156` n `20`; unknown avg `0.2646` n `940`
- 4h: commodity avg `0.0168` n `12`; crypto_alt avg `1.6116` n `234`; crypto_major avg `0.4444` n `8`; equity avg `0.0404` n `140`; fx avg `0.0112` n `6`; index avg `-0.0119` n `26`; metal avg `0.0176` n `20`; unknown avg `0.6942` n `934`
- 24h: commodity avg `0.2337` n `12`; crypto_alt avg `4.1836` n `234`; crypto_major avg `3.779` n `8`; equity avg `0.4455` n `140`; fx avg `0.0011` n `6`; index avg `-0.0082` n `26`; metal avg `-0.2015` n `20`; unknown avg `2.3823` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
