# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T04:07:31.022711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0221` n `13`; crypto_alt avg `0.2377` n `237`; crypto_major avg `0.3601` n `8`; equity avg `0.142` n `152`; fx avg `-0.0038` n `6`; index avg `0.0201` n `26`; metal avg `-0.0175` n `20`; unknown avg `0.331` n `1232`
- 1h: commodity avg `-0.0226` n `13`; crypto_alt avg `-0.5943` n `237`; crypto_major avg `-0.3165` n `8`; equity avg `-0.0493` n `152`; fx avg `0.0066` n `6`; index avg `0.0021` n `26`; metal avg `-0.0283` n `20`; unknown avg `-0.0647` n `1234`
- 4h: commodity avg `-0.2004` n `13`; crypto_alt avg `-1.0889` n `237`; crypto_major avg `-0.6935` n `8`; equity avg `-0.7185` n `152`; fx avg `-0.0168` n `6`; index avg `-0.0192` n `26`; metal avg `0.0591` n `20`; unknown avg `1.3473` n `1162`
- 24h: commodity avg `-0.6501` n `13`; crypto_alt avg `-1.9277` n `237`; crypto_major avg `-1.5838` n `8`; equity avg `-0.7602` n `152`; fx avg `0.0466` n `6`; index avg `-0.0031` n `26`; metal avg `0.1634` n `20`; unknown avg `-0.4101` n `987`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2479`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
