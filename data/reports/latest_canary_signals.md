# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T22:07:32.505317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2151` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `-0.2572` n `234`; crypto_major avg `-0.2166` n `8`; equity avg `-0.0198` n `140`; fx avg `0.0052` n `6`; index avg `-0.0047` n `26`; metal avg `0.0019` n `20`; unknown avg `0.1296` n `941`
- 1h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.6562` n `234`; crypto_major avg `-0.6531` n `8`; equity avg `-0.0276` n `140`; fx avg `0.0114` n `6`; index avg `-0.0113` n `26`; metal avg `0.0014` n `20`; unknown avg `0.2838` n `941`
- 4h: commodity avg `0.0332` n `12`; crypto_alt avg `-1.1464` n `234`; crypto_major avg `-1.1992` n `8`; equity avg `0.0945` n `140`; fx avg `-0.0323` n `6`; index avg `0.0159` n `26`; metal avg `0.0077` n `20`; unknown avg `65.1947` n `919`
- 24h: commodity avg `0.101` n `12`; crypto_alt avg `0.1957` n `234`; crypto_major avg `-0.8095` n `8`; equity avg `-0.0867` n `140`; fx avg `-0.0556` n `6`; index avg `0.0173` n `26`; metal avg `-0.0057` n `20`; unknown avg `1.7717` n `846`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
