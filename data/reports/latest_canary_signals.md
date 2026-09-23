# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T22:52:26.318132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `12`; crypto_alt avg `0.2838` n `234`; crypto_major avg `0.2602` n `8`; equity avg `0.0531` n `141`; fx avg `0.0109` n `6`; index avg `0.0025` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.1564` n `945`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `0.1613` n `234`; crypto_major avg `0.3272` n `8`; equity avg `0.0932` n `141`; fx avg `0.0089` n `6`; index avg `0.0118` n `26`; metal avg `-0.0104` n `20`; unknown avg `1.4577` n `943`
- 4h: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.2778` n `234`; crypto_major avg `0.3408` n `8`; equity avg `-0.0966` n `141`; fx avg `-0.0098` n `6`; index avg `0.0102` n `26`; metal avg `0.0336` n `20`; unknown avg `0.5403` n `845`
- 24h: commodity avg `0.5157` n `12`; crypto_alt avg `-4.2298` n `234`; crypto_major avg `-3.1834` n `8`; equity avg `-1.5539` n `140`; fx avg `-0.0023` n `6`; index avg `-0.353` n `26`; metal avg `-0.813` n `20`; unknown avg `584.3522` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
