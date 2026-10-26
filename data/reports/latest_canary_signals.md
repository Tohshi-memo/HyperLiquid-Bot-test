# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T15:07:33.418286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `0.5769` n `237`; crypto_major avg `0.4253` n `8`; equity avg `0.395` n `153`; fx avg `-0.0027` n `6`; index avg `0.0487` n `26`; metal avg `0.0543` n `20`; unknown avg `0.0444` n `1238`
- 1h: commodity avg `0.0995` n `13`; crypto_alt avg `1.4197` n `237`; crypto_major avg `1.1274` n `8`; equity avg `1.8122` n `153`; fx avg `0.033` n `6`; index avg `0.272` n `26`; metal avg `0.2772` n `20`; unknown avg `629.9234` n `1174`
- 4h: commodity avg `0.0605` n `13`; crypto_alt avg `1.4688` n `237`; crypto_major avg `0.8891` n `8`; equity avg `1.822` n `152`; fx avg `0.0162` n `6`; index avg `0.3285` n `26`; metal avg `0.15` n `20`; unknown avg `627.5372` n `1156`
- 24h: commodity avg `-0.305` n `13`; crypto_alt avg `0.9019` n `237`; crypto_major avg `0.4772` n `8`; equity avg `0.9438` n `152`; fx avg `0.0546` n `6`; index avg `0.2492` n `26`; metal avg `0.2158` n `20`; unknown avg `804.013` n `926`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2329`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2009`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1964`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1818`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1281`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `669`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0787`, n `669`, weak_sample_signal
