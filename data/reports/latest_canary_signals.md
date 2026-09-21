# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T01:37:31.783250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0729` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `-0.7667` n `234`; crypto_major avg `-0.6973` n `8`; equity avg `0.0065` n `140`; fx avg `0.032` n `6`; index avg `0.0043` n `26`; metal avg `0.023` n `20`; unknown avg `3.5696` n `944`
- 1h: commodity avg `-0.2267` n `12`; crypto_alt avg `-0.4949` n `234`; crypto_major avg `-0.2614` n `8`; equity avg `0.15` n `140`; fx avg `0.0091` n `6`; index avg `0.0201` n `26`; metal avg `0.0852` n `20`; unknown avg `1.6239` n `941`
- 4h: commodity avg `-0.6839` n `12`; crypto_alt avg `0.7732` n `234`; crypto_major avg `1.389` n `8`; equity avg `0.9847` n `140`; fx avg `0.0505` n `6`; index avg `0.1503` n `26`; metal avg `0.1547` n `20`; unknown avg `1.5467` n `907`
- 24h: commodity avg `-0.5052` n `12`; crypto_alt avg `1.7462` n `234`; crypto_major avg `1.7043` n `8`; equity avg `0.8764` n `140`; fx avg `0.0203` n `6`; index avg `0.1241` n `26`; metal avg `0.099` n `20`; unknown avg `3.8696` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
