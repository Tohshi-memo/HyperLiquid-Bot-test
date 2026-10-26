# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T17:18:32.184932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1` n `13`; crypto_alt avg `0.2982` n `237`; crypto_major avg `0.2025` n `8`; equity avg `0.2459` n `154`; fx avg `0.0232` n `6`; index avg `0.0446` n `27`; metal avg `0.0046` n `20`; unknown avg `-0.0989` n `1238`
- 1h: commodity avg `-0.2553` n `13`; crypto_alt avg `0.4921` n `237`; crypto_major avg `0.4833` n `8`; equity avg `0.381` n `154`; fx avg `0.0045` n `6`; index avg `0.0601` n `27`; metal avg `0.059` n `20`; unknown avg `0.2039` n `1238`
- 4h: commodity avg `0.0614` n `13`; crypto_alt avg `0.8885` n `237`; crypto_major avg `0.7954` n `8`; equity avg `1.6475` n `153`; fx avg `0.0257` n `6`; index avg `0.2583` n `27`; metal avg `0.1481` n `20`; unknown avg `595.7715` n `1166`
- 24h: commodity avg `-0.1623` n `13`; crypto_alt avg `-0.1634` n `237`; crypto_major avg `0.0853` n `8`; equity avg `1.0434` n `153`; fx avg `0.0699` n `6`; index avg `-0.0127` n `27`; metal avg `0.152` n `20`; unknown avg `781.6588` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
