# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T02:52:24.526677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.4628` n `232`; crypto_major avg `0.1742` n `8`; equity avg `0.0193` n `134`; fx avg `0.0348` n `6`; index avg `-0.0155` n `26`; metal avg `-0.0196` n `20`; unknown avg `0.1231` n `766`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `0.9207` n `232`; crypto_major avg `0.6989` n `8`; equity avg `0.1964` n `134`; fx avg `0.0613` n `6`; index avg `-0.008` n `26`; metal avg `-0.0165` n `20`; unknown avg `1.2688` n `764`
- 4h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.3539` n `232`; crypto_major avg `0.2645` n `8`; equity avg `0.2793` n `134`; fx avg `0.002` n `6`; index avg `0.0059` n `26`; metal avg `-0.0386` n `20`; unknown avg `2.2177` n `756`
- 24h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.906` n `232`; crypto_major avg `0.523` n `8`; equity avg `0.4594` n `134`; fx avg `0.0382` n `6`; index avg `0.0079` n `26`; metal avg `-0.0741` n `20`; unknown avg `1.016` n `650`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
