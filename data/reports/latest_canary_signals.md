# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T08:37:27.521838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.3831` n `234`; crypto_major avg `0.3464` n `8`; equity avg `0.0203` n `141`; fx avg `0.0022` n `6`; index avg `0.0001` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.441` n `961`
- 1h: commodity avg `-0.0445` n `12`; crypto_alt avg `0.1445` n `234`; crypto_major avg `0.2698` n `8`; equity avg `0.0253` n `141`; fx avg `-0.0005` n `6`; index avg `-0.002` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.109` n `943`
- 4h: commodity avg `-0.0796` n `12`; crypto_alt avg `1.06` n `234`; crypto_major avg `0.2579` n `8`; equity avg `0.0715` n `141`; fx avg `0.0118` n `6`; index avg `0.0017` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.0415` n `919`
- 24h: commodity avg `0.0192` n `12`; crypto_alt avg `2.5819` n `234`; crypto_major avg `0.5368` n `8`; equity avg `-0.8279` n `141`; fx avg `-0.0691` n `6`; index avg `0.0164` n `26`; metal avg `0.0844` n `20`; unknown avg `1122.5903` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
