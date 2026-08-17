# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T07:22:28.611132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.0683` n `230`; crypto_major avg `-0.0084` n `8`; equity avg `-0.0752` n `114`; fx avg `0.0077` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.0006` n `792`
- 1h: commodity avg `-0.0509` n `12`; crypto_alt avg `0.0761` n `230`; crypto_major avg `0.1751` n `8`; equity avg `0.0771` n `114`; fx avg `0.0057` n `6`; index avg `0.0033` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0121` n `792`
- 4h: commodity avg `-0.1619` n `12`; crypto_alt avg `0.1661` n `230`; crypto_major avg `0.3641` n `8`; equity avg `0.4944` n `114`; fx avg `0.0063` n `6`; index avg `0.0819` n `25`; metal avg `0.0168` n `20`; unknown avg `0.1409` n `776`
- 24h: commodity avg `-0.2633` n `12`; crypto_alt avg `0.3361` n `230`; crypto_major avg `0.9641` n `8`; equity avg `1.0738` n `114`; fx avg `-0.0281` n `6`; index avg `0.1269` n `25`; metal avg `0.2071` n `20`; unknown avg `0.1386` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
