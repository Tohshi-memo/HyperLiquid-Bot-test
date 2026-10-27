# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T03:22:26.631639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `13`; crypto_alt avg `0.0091` n `237`; crypto_major avg `0.0174` n `8`; equity avg `-0.0377` n `154`; fx avg `0.0057` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0226` n `20`; unknown avg `3.1414` n `1238`
- 1h: commodity avg `0.0066` n `13`; crypto_alt avg `-0.4986` n `237`; crypto_major avg `-0.3713` n `8`; equity avg `-0.327` n `154`; fx avg `0.0316` n `6`; index avg `-0.0562` n `27`; metal avg `-0.1115` n `20`; unknown avg `3.2343` n `1232`
- 4h: commodity avg `-0.0871` n `13`; crypto_alt avg `-0.5426` n `237`; crypto_major avg `-0.1094` n `8`; equity avg `0.0139` n `154`; fx avg `0.0271` n `6`; index avg `0.0578` n `27`; metal avg `-0.1187` n `20`; unknown avg `1.2333` n `1224`
- 24h: commodity avg `0.0697` n `13`; crypto_alt avg `-0.0013` n `237`; crypto_major avg `0.5444` n `8`; equity avg `1.7076` n `153`; fx avg `0.0226` n `6`; index avg `0.084` n `27`; metal avg `-0.2305` n `20`; unknown avg `1000.0107` n `1000`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
