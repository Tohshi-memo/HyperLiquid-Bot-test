# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T10:07:27.753871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.36` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0416` n `234`; crypto_major avg `-0.0578` n `8`; equity avg `-0.0023` n `140`; fx avg `0.0021` n `6`; index avg `0.0012` n `26`; metal avg `0.0057` n `20`; unknown avg `0.3418` n `940`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `0.0686` n `234`; crypto_major avg `-0.2575` n `8`; equity avg `-0.0011` n `140`; fx avg `0.0064` n `6`; index avg `-0.0003` n `26`; metal avg `0.0088` n `20`; unknown avg `0.1383` n `940`
- 4h: commodity avg `0.0045` n `12`; crypto_alt avg `1.0943` n `234`; crypto_major avg `-0.0837` n `8`; equity avg `0.0467` n `140`; fx avg `0.0272` n `6`; index avg `0.0343` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.8242` n `934`
- 24h: commodity avg `0.1588` n `12`; crypto_alt avg `3.0741` n `234`; crypto_major avg `3.3163` n `8`; equity avg `0.2771` n `140`; fx avg `-0.0328` n `6`; index avg `0.0036` n `26`; metal avg `-0.1692` n `20`; unknown avg `2.3803` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
