# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T09:22:29.179181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.36` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.086` n `234`; crypto_major avg `0.0593` n `8`; equity avg `-0.0123` n `140`; fx avg `0.0018` n `6`; index avg `0.0003` n `26`; metal avg `0.0084` n `20`; unknown avg `-0.0544` n `942`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `0.1839` n `234`; crypto_major avg `0.0294` n `8`; equity avg `-0.0255` n `140`; fx avg `0.0166` n `6`; index avg `0.0166` n `26`; metal avg `-0.0055` n `20`; unknown avg `1.8704` n `940`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.3048` n `234`; crypto_major avg `0.1083` n `8`; equity avg `-0.0229` n `140`; fx avg `0.0289` n `6`; index avg `0.0146` n `26`; metal avg `-0.007` n `20`; unknown avg `1.957` n `898`
- 24h: commodity avg `0.3007` n `12`; crypto_alt avg `3.1315` n `234`; crypto_major avg `3.622` n `8`; equity avg `0.0873` n `140`; fx avg `0.0095` n `6`; index avg `-0.0509` n `26`; metal avg `-0.2694` n `20`; unknown avg `2.2058` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
