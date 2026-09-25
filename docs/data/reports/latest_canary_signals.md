# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T21:31:18.916725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1875` n `234`; crypto_major avg `0.1382` n `8`; equity avg `0.0578` n `141`; fx avg `0.0` n `6`; index avg `0.0131` n `26`; metal avg `0.0154` n `20`; unknown avg `0.5947` n `960`
- 1h: commodity avg `-0.0374` n `12`; crypto_alt avg `-0.8959` n `234`; crypto_major avg `-0.4685` n `8`; equity avg `0.0212` n `141`; fx avg `-0.0128` n `6`; index avg `0.0122` n `26`; metal avg `0.0142` n `20`; unknown avg `-0.1915` n `956`
- 4h: commodity avg `0.0382` n `12`; crypto_alt avg `0.5257` n `234`; crypto_major avg `0.243` n `8`; equity avg `-0.0451` n `141`; fx avg `-0.0167` n `6`; index avg `0.0419` n `26`; metal avg `0.0518` n `20`; unknown avg `-0.0303` n `876`
- 24h: commodity avg `-0.6368` n `12`; crypto_alt avg `1.4336` n `234`; crypto_major avg `0.3035` n `8`; equity avg `0.1053` n `141`; fx avg `-0.2376` n `6`; index avg `0.2548` n `26`; metal avg `0.1917` n `20`; unknown avg `1147.436` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
