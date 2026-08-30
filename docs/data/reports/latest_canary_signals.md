# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T00:22:25.056778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.0486` n `231`; crypto_major avg `0.0901` n `8`; equity avg `0.0075` n `128`; fx avg `0.0006` n `6`; index avg `0.028` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.0424` n `793`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `0.0688` n `231`; crypto_major avg `0.0408` n `8`; equity avg `0.0057` n `128`; fx avg `0.0147` n `6`; index avg `0.0085` n `26`; metal avg `0.0033` n `20`; unknown avg `0.0047` n `793`
- 4h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0076` n `231`; crypto_major avg `0.1047` n `8`; equity avg `0.0368` n `128`; fx avg `0.0177` n `6`; index avg `0.0334` n `26`; metal avg `0.0128` n `20`; unknown avg `-0.0439` n `774`
- 24h: commodity avg `0.0271` n `12`; crypto_alt avg `0.116` n `231`; crypto_major avg `0.7109` n `8`; equity avg `0.3797` n `128`; fx avg `-0.0043` n `6`; index avg `0.1048` n `26`; metal avg `0.0891` n `20`; unknown avg `0.1514` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
