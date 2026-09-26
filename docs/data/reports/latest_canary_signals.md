# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T02:22:27.245528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.106` n `234`; crypto_major avg `-0.0379` n `8`; equity avg `0.0048` n `141`; fx avg `-0.0015` n `6`; index avg `0.0043` n `26`; metal avg `0.0002` n `20`; unknown avg `0.7775` n `960`
- 1h: commodity avg `-0.0696` n `12`; crypto_alt avg `0.0091` n `234`; crypto_major avg `0.0468` n `8`; equity avg `0.0666` n `141`; fx avg `0.0006` n `6`; index avg `0.0201` n `26`; metal avg `0.0169` n `20`; unknown avg `2.5111` n `958`
- 4h: commodity avg `0.2707` n `12`; crypto_alt avg `0.4238` n `234`; crypto_major avg `0.2114` n `8`; equity avg `-0.1316` n `141`; fx avg `0.0005` n `6`; index avg `-0.0412` n `26`; metal avg `-0.0024` n `20`; unknown avg `2.6713` n `952`
- 24h: commodity avg `0.0762` n `12`; crypto_alt avg `2.7392` n `234`; crypto_major avg `0.7882` n `8`; equity avg `-0.4078` n `141`; fx avg `-0.1461` n `6`; index avg `0.1246` n `26`; metal avg `0.1` n `20`; unknown avg `1126.3127` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
