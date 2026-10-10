# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T02:37:34.207790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `13`; crypto_alt avg `0.0847` n `235`; crypto_major avg `0.0401` n `8`; equity avg `0.0231` n `150`; fx avg `0.0036` n `6`; index avg `0.001` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2497` n `1116`
- 1h: commodity avg `-0.0464` n `13`; crypto_alt avg `0.4996` n `235`; crypto_major avg `0.1922` n `8`; equity avg `0.0062` n `150`; fx avg `0.001` n `6`; index avg `-0.0047` n `26`; metal avg `-0.003` n `20`; unknown avg `0.112` n `1114`
- 4h: commodity avg `0.006` n `13`; crypto_alt avg `1.2471` n `235`; crypto_major avg `0.3783` n `8`; equity avg `0.0743` n `150`; fx avg `0.0068` n `6`; index avg `0.028` n `26`; metal avg `0.0209` n `20`; unknown avg `0.056` n `1108`
- 24h: commodity avg `-0.0489` n `13`; crypto_alt avg `2.9929` n `235`; crypto_major avg `0.7493` n `8`; equity avg `0.5439` n `150`; fx avg `-0.0204` n `6`; index avg `0.0827` n `26`; metal avg `0.1705` n `20`; unknown avg `12.9877` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
