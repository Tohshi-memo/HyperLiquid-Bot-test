# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T23:07:36.952757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.0143` n `234`; crypto_major avg `-0.0919` n `8`; equity avg `-0.023` n `141`; fx avg `-0.0075` n `6`; index avg `-0.0018` n `26`; metal avg `0.0082` n `20`; unknown avg `-0.0826` n `943`
- 1h: commodity avg `-0.0598` n `12`; crypto_alt avg `-0.3777` n `234`; crypto_major avg `-0.258` n `8`; equity avg `-0.0113` n `141`; fx avg `-0.0035` n `6`; index avg `-0.0279` n `26`; metal avg `-0.0046` n `20`; unknown avg `1.0549` n `943`
- 4h: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0247` n `234`; crypto_major avg `0.3125` n `8`; equity avg `-0.1182` n `141`; fx avg `-0.0138` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0475` n `20`; unknown avg `-0.3077` n `845`
- 24h: commodity avg `0.5124` n `12`; crypto_alt avg `-4.5479` n `234`; crypto_major avg `-3.5714` n `8`; equity avg `-1.5917` n `140`; fx avg `-0.0063` n `6`; index avg `-0.3549` n `26`; metal avg `-0.8204` n `20`; unknown avg `584.4632` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
