# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T20:22:28.037524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0312` n `12`; crypto_alt avg `0.2838` n `234`; crypto_major avg `0.1057` n `8`; equity avg `-0.0055` n `141`; fx avg `0.0007` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0031` n `20`; unknown avg `2.8606` n `936`
- 1h: commodity avg `0.0419` n `12`; crypto_alt avg `0.3285` n `234`; crypto_major avg `0.0242` n `8`; equity avg `-0.1081` n `141`; fx avg `0.0031` n `6`; index avg `0.0064` n `26`; metal avg `-0.0205` n `20`; unknown avg `134.6332` n `900`
- 4h: commodity avg `0.2135` n `12`; crypto_alt avg `0.9835` n `234`; crypto_major avg `0.2641` n `8`; equity avg `-0.1954` n `141`; fx avg `0.0191` n `6`; index avg `0.0216` n `26`; metal avg `-0.002` n `20`; unknown avg `5.9479` n `900`
- 24h: commodity avg `-0.666` n `12`; crypto_alt avg `2.3851` n `234`; crypto_major avg `0.7521` n `8`; equity avg `0.2148` n `141`; fx avg `-0.2415` n `6`; index avg `0.2633` n `26`; metal avg `0.2047` n `20`; unknown avg `1145.7836` n `796`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
