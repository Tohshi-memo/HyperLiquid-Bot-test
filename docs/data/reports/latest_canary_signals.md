# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T23:22:23.498761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `13`; crypto_alt avg `0.0621` n `239`; crypto_major avg `0.0156` n `8`; equity avg `-0.0088` n `158`; fx avg `0.0089` n `6`; index avg `0.0055` n `27`; metal avg `-0.0057` n `20`; unknown avg `-0.1063` n `1262`
- 1h: commodity avg `0.0041` n `13`; crypto_alt avg `0.1385` n `239`; crypto_major avg `-0.0094` n `8`; equity avg `0.0495` n `158`; fx avg `-0.002` n `6`; index avg `0.006` n `27`; metal avg `-0.0021` n `20`; unknown avg `0.3266` n `1240`
- 4h: commodity avg `0.0637` n `13`; crypto_alt avg `-0.2611` n `239`; crypto_major avg `-0.2108` n `8`; equity avg `-0.103` n `158`; fx avg `0.0053` n `6`; index avg `-0.0074` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.7271` n `1198`
- 24h: commodity avg `0.0536` n `13`; crypto_alt avg `-1.206` n `239`; crypto_major avg `-0.6303` n `8`; equity avg `-0.0723` n `158`; fx avg `-0.0174` n `6`; index avg `0.0547` n `27`; metal avg `-0.0354` n `20`; unknown avg `160.3215` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
