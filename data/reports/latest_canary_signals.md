# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T03:22:32.482136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5742` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.527` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.0686` n `234`; crypto_major avg `-0.0317` n `8`; equity avg `-0.0218` n `140`; fx avg `-0.0032` n `6`; index avg `0.0046` n `26`; metal avg `0.006` n `20`; unknown avg `0.1219` n `944`
- 1h: commodity avg `0.0931` n `12`; crypto_alt avg `-0.2824` n `234`; crypto_major avg `-0.3491` n `8`; equity avg `0.0094` n `140`; fx avg `0.0095` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0429` n `20`; unknown avg `0.1188` n `942`
- 4h: commodity avg `0.2058` n `12`; crypto_alt avg `-0.5078` n `234`; crypto_major avg `-1.5326` n `8`; equity avg `0.0416` n `140`; fx avg `-0.1516` n `6`; index avg `-0.0056` n `26`; metal avg `-0.1449` n `20`; unknown avg `1.128` n `936`
- 24h: commodity avg `-0.0857` n `12`; crypto_alt avg `2.8346` n `234`; crypto_major avg `3.7832` n `8`; equity avg `2.3371` n `140`; fx avg `-0.1985` n `6`; index avg `0.4719` n `26`; metal avg `-0.0408` n `20`; unknown avg `8.4296` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
