# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T09:52:25.666843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `80.61` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.2716` n `234`; crypto_major avg `0.162` n `8`; equity avg `0.035` n `140`; fx avg `-0.0041` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.1686` n `942`
- 1h: commodity avg `-0.023` n `12`; crypto_alt avg `0.1944` n `234`; crypto_major avg `-0.1926` n `8`; equity avg `0.0003` n `140`; fx avg `0.0292` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0046` n `20`; unknown avg `-0.044` n `940`
- 4h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.9856` n `234`; crypto_major avg `-0.1898` n `8`; equity avg `0.0106` n `140`; fx avg `0.0073` n `6`; index avg `0.0205` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.3416` n `898`
- 24h: commodity avg `0.1439` n `12`; crypto_alt avg `3.2592` n `234`; crypto_major avg `3.4836` n `8`; equity avg `0.3081` n `140`; fx avg `-0.0531` n `6`; index avg `-0.0117` n `26`; metal avg `-0.1502` n `20`; unknown avg `2.2925` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
