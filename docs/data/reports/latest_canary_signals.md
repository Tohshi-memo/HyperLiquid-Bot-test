# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T08:37:30.802659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0889` n `13`; crypto_alt avg `0.0592` n `239`; crypto_major avg `-0.1231` n `8`; equity avg `0.0271` n `160`; fx avg `-0.0049` n `6`; index avg `0.0127` n `27`; metal avg `0.0227` n `20`; unknown avg `0.3045` n `1261`
- 1h: commodity avg `-0.1339` n `13`; crypto_alt avg `-0.11` n `239`; crypto_major avg `-0.5212` n `8`; equity avg `0.2405` n `160`; fx avg `0.0041` n `6`; index avg `0.0262` n `27`; metal avg `0.0609` n `20`; unknown avg `-0.053` n `1239`
- 4h: commodity avg `-0.2553` n `13`; crypto_alt avg `0.277` n `239`; crypto_major avg `-0.0592` n `8`; equity avg `0.3729` n `160`; fx avg `-0.0675` n `6`; index avg `0.0919` n `27`; metal avg `-0.1039` n `20`; unknown avg `1.6898` n `1211`
- 24h: commodity avg `-0.6393` n `13`; crypto_alt avg `2.1177` n `239`; crypto_major avg `0.4827` n `8`; equity avg `4.9439` n `160`; fx avg `-0.0636` n `6`; index avg `0.562` n `27`; metal avg `0.2239` n `20`; unknown avg `172.3053` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
