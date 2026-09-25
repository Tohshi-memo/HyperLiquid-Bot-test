# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T10:52:31.194762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `0.0994` n `234`; crypto_major avg `0.1167` n `8`; equity avg `-0.0037` n `141`; fx avg `0.0003` n `6`; index avg `-0.0059` n `26`; metal avg `0.0408` n `20`; unknown avg `-0.0058` n `946`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.3195` n `234`; crypto_major avg `0.3775` n `8`; equity avg `0.0313` n `141`; fx avg `-0.0195` n `6`; index avg `-0.0161` n `26`; metal avg `0.1743` n `20`; unknown avg `0.7126` n `944`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `1.9313` n `234`; crypto_major avg `1.4454` n `8`; equity avg `0.2546` n `141`; fx avg `-0.0368` n `6`; index avg `0.0306` n `26`; metal avg `0.2946` n `20`; unknown avg `2.768` n `926`
- 24h: commodity avg `0.1382` n `12`; crypto_alt avg `5.2669` n `234`; crypto_major avg `3.1053` n `8`; equity avg `1.7622` n `141`; fx avg `-0.2315` n `6`; index avg `0.25` n `26`; metal avg `0.3507` n `20`; unknown avg `12.3707` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
