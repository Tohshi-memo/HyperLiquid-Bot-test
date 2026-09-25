# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T13:02:08.054442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.2521` n `234`; crypto_major avg `0.0223` n `8`; equity avg `-0.0266` n `141`; fx avg `-0.0237` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0561` n `20`; unknown avg `60.7333` n `942`
- 1h: commodity avg `0.1195` n `12`; crypto_alt avg `-0.0122` n `234`; crypto_major avg `-0.3198` n `8`; equity avg `-0.1603` n `141`; fx avg `0.0002` n `6`; index avg `-0.0489` n `26`; metal avg `-0.1406` n `20`; unknown avg `19.5446` n `942`
- 4h: commodity avg `0.127` n `12`; crypto_alt avg `0.9814` n `234`; crypto_major avg `0.9735` n `8`; equity avg `-0.2244` n `141`; fx avg `-0.005` n `6`; index avg `-0.0538` n `26`; metal avg `-0.0415` n `20`; unknown avg `5.2253` n `936`
- 24h: commodity avg `0.105` n `12`; crypto_alt avg `5.0243` n `234`; crypto_major avg `3.178` n `8`; equity avg `1.6885` n `141`; fx avg `-0.1688` n `6`; index avg `0.2338` n `26`; metal avg `0.1102` n `20`; unknown avg `15.7534` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
