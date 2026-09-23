# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T20:37:27.441822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `12`; crypto_alt avg `-0.1906` n `234`; crypto_major avg `-0.1099` n `8`; equity avg `0.0052` n `141`; fx avg `0.003` n `6`; index avg `0.0057` n `26`; metal avg `0.0082` n `20`; unknown avg `5.0133` n `935`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `-0.464` n `234`; crypto_major avg `-0.3768` n `8`; equity avg `-0.1925` n `141`; fx avg `0.0071` n `6`; index avg `-0.0015` n `26`; metal avg `0.0249` n `20`; unknown avg `1.2831` n `861`
- 4h: commodity avg `0.1691` n `12`; crypto_alt avg `-1.0024` n `234`; crypto_major avg `-0.3295` n `8`; equity avg `-0.3704` n `141`; fx avg `-0.0058` n `6`; index avg `-0.0283` n `26`; metal avg `-0.0221` n `20`; unknown avg `6.5111` n `853`
- 24h: commodity avg `0.642` n `12`; crypto_alt avg `-3.9393` n `234`; crypto_major avg `-3.6846` n `8`; equity avg `-1.6272` n `140`; fx avg `0.0288` n `6`; index avg `-0.3541` n `26`; metal avg `-0.8345` n `20`; unknown avg `575.1675` n `836`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
