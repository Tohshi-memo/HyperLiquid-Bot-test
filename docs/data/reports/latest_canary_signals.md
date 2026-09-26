# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T22:22:26.686710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.1204` n `234`; crypto_major avg `-0.1022` n `8`; equity avg `-0.0062` n `141`; fx avg `0.0003` n `6`; index avg `0.0034` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.1159` n `961`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.2584` n `234`; crypto_major avg `0.178` n `8`; equity avg `0.0391` n `141`; fx avg `-0.0043` n `6`; index avg `0.0059` n `26`; metal avg `0.0004` n `20`; unknown avg `1.166` n `935`
- 4h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.8608` n `234`; crypto_major avg `-0.183` n `8`; equity avg `-0.0003` n `141`; fx avg `-0.0102` n `6`; index avg `0.0025` n `26`; metal avg `0.0095` n `20`; unknown avg `160.0629` n `929`
- 24h: commodity avg `0.3091` n `12`; crypto_alt avg `0.8692` n `234`; crypto_major avg `-0.6527` n `8`; equity avg `-0.0233` n `141`; fx avg `0.0187` n `6`; index avg `-0.0531` n `26`; metal avg `-0.0148` n `20`; unknown avg `5.1942` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
