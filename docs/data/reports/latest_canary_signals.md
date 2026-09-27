# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T12:07:26.969804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.1588` n `234`; crypto_major avg `0.164` n `8`; equity avg `0.0126` n `141`; fx avg `0.0006` n `6`; index avg `-0.0006` n `26`; metal avg `-0.003` n `20`; unknown avg `1.0003` n `954`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `0.2651` n `234`; crypto_major avg `0.2425` n `8`; equity avg `0.0177` n `141`; fx avg `-0.0074` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0038` n `20`; unknown avg `1.4767` n `954`
- 4h: commodity avg `0.0575` n `12`; crypto_alt avg `-0.1068` n `234`; crypto_major avg `0.0455` n `8`; equity avg `0.0382` n `141`; fx avg `-0.0163` n `6`; index avg `0.0022` n `26`; metal avg `-0.0148` n `20`; unknown avg `1.2596` n `953`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `0.8245` n `234`; crypto_major avg `0.8612` n `8`; equity avg `0.3597` n `141`; fx avg `-0.0357` n `6`; index avg `0.0282` n `26`; metal avg `-0.0122` n `20`; unknown avg `38.8826` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
