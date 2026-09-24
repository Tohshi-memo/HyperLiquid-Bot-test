# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T05:22:31.942836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `-0.2654` n `234`; crypto_major avg `-0.2679` n `8`; equity avg `-0.109` n `141`; fx avg `-0.0029` n `6`; index avg `-0.0152` n `26`; metal avg `-0.0316` n `20`; unknown avg `325.1599` n `945`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `1.1473` n `234`; crypto_major avg `0.8158` n `8`; equity avg `0.2077` n `141`; fx avg `-0.0302` n `6`; index avg `0.0172` n `26`; metal avg `0.0334` n `20`; unknown avg `8.9579` n `943`
- 4h: commodity avg `0.0709` n `12`; crypto_alt avg `1.8696` n `234`; crypto_major avg `0.4729` n `8`; equity avg `-0.1633` n `141`; fx avg `0.0018` n `6`; index avg `-0.0463` n `26`; metal avg `0.0173` n `20`; unknown avg `1.5671` n `937`
- 24h: commodity avg `0.5706` n `12`; crypto_alt avg `-3.8025` n `234`; crypto_major avg `-3.8499` n `8`; equity avg `-1.8011` n `140`; fx avg `0.0772` n `6`; index avg `-0.357` n `26`; metal avg `-0.6046` n `20`; unknown avg `585.0044` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
