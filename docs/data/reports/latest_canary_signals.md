# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T22:37:30.716402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.0689` n `235`; crypto_major avg `0.0322` n `8`; equity avg `-0.0122` n `150`; fx avg `0.0005` n `6`; index avg `-0.0015` n `26`; metal avg `0.0008` n `20`; unknown avg `0.1846` n `1117`
- 1h: commodity avg `0.1484` n `13`; crypto_alt avg `-0.0989` n `235`; crypto_major avg `-0.0533` n `8`; equity avg `-0.0075` n `150`; fx avg `0.0067` n `6`; index avg `0.0051` n `26`; metal avg `0.0077` n `20`; unknown avg `0.429` n `1091`
- 4h: commodity avg `0.199` n `13`; crypto_alt avg `0.3793` n `235`; crypto_major avg `0.0555` n `8`; equity avg `0.0718` n `150`; fx avg `-0.0009` n `6`; index avg `0.0123` n `26`; metal avg `0.0153` n `20`; unknown avg `-0.1399` n `983`
- 24h: commodity avg `0.0892` n `13`; crypto_alt avg `2.4813` n `235`; crypto_major avg `0.7701` n `8`; equity avg `0.1895` n `150`; fx avg `-0.0033` n `6`; index avg `0.0218` n `26`; metal avg `0.0158` n `20`; unknown avg `0.1642` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
