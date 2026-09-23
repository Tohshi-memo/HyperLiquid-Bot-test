# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T21:22:35.827984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0378` n `12`; crypto_alt avg `0.0271` n `234`; crypto_major avg `0.049` n `8`; equity avg `-0.0049` n `141`; fx avg `0.0042` n `6`; index avg `-0.0077` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.0326` n `929`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.2593` n `234`; crypto_major avg `-0.0838` n `8`; equity avg `0.0148` n `141`; fx avg `-0.0102` n `6`; index avg `0.0017` n `26`; metal avg `0.0402` n `20`; unknown avg `-0.2775` n `917`
- 4h: commodity avg `0.3045` n `12`; crypto_alt avg `-1.1024` n `234`; crypto_major avg `-0.2479` n `8`; equity avg `-0.1494` n `141`; fx avg `-0.0268` n `6`; index avg `0.0153` n `26`; metal avg `0.09` n `20`; unknown avg `3.4942` n `845`
- 24h: commodity avg `0.612` n `12`; crypto_alt avg `-3.869` n `234`; crypto_major avg `-3.4614` n `8`; equity avg `-1.5931` n `140`; fx avg `0.0081` n `6`; index avg `-0.3543` n `26`; metal avg `-0.7746` n `20`; unknown avg `584.0541` n `820`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
