# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T11:22:30.454292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.33` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.1403` n `234`; crypto_major avg `0.1095` n `8`; equity avg `0.0062` n `140`; fx avg `0.0021` n `6`; index avg `0.0017` n `26`; metal avg `0.007` n `20`; unknown avg `0.0314` n `942`
- 1h: commodity avg `0.0174` n `12`; crypto_alt avg `0.4002` n `234`; crypto_major avg `0.2217` n `8`; equity avg `-0.0132` n `140`; fx avg `-0.0075` n `6`; index avg `-0.0177` n `26`; metal avg `0.0094` n `20`; unknown avg `0.228` n `940`
- 4h: commodity avg `0.011` n `12`; crypto_alt avg `1.4589` n `234`; crypto_major avg `0.3392` n `8`; equity avg `0.0087` n `140`; fx avg `0.0003` n `6`; index avg `-0.0272` n `26`; metal avg `0.0043` n `20`; unknown avg `0.7047` n `934`
- 24h: commodity avg `0.1777` n `12`; crypto_alt avg `4.6263` n `234`; crypto_major avg `4.0375` n `8`; equity avg `0.4582` n `140`; fx avg `-0.0138` n `6`; index avg `0.0124` n `26`; metal avg `-0.2032` n `20`; unknown avg `2.4045` n `803`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
