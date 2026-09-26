# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T00:22:29.606392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.2401` n `234`; crypto_major avg `0.057` n `8`; equity avg `-0.0063` n `141`; fx avg `0.0044` n `6`; index avg `0.0015` n `26`; metal avg `0.0001` n `20`; unknown avg `-0.0091` n `960`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `0.1113` n `234`; crypto_major avg `-0.0959` n `8`; equity avg `-0.013` n `141`; fx avg `0.0014` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.2089` n `952`
- 4h: commodity avg `-0.013` n `12`; crypto_alt avg `0.6839` n `234`; crypto_major avg `0.2241` n `8`; equity avg `0.0836` n `141`; fx avg `-0.014` n `6`; index avg `0.0246` n `26`; metal avg `0.0029` n `20`; unknown avg `0.2712` n `898`
- 24h: commodity avg `-0.3238` n `12`; crypto_alt avg `3.058` n `234`; crypto_major avg `0.9424` n `8`; equity avg `0.0197` n `141`; fx avg `-0.2477` n `6`; index avg `0.2473` n `26`; metal avg `0.2104` n `20`; unknown avg `1125.6832` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
