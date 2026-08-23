# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T18:22:26.304548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.2585` n `231`; crypto_major avg `0.3198` n `8`; equity avg `0.0255` n `122`; fx avg `0.008` n `6`; index avg `0.0146` n `25`; metal avg `-0.0` n `20`; unknown avg `0.2631` n `793`
- 1h: commodity avg `-0.037` n `12`; crypto_alt avg `-0.1263` n `231`; crypto_major avg `-0.1899` n `8`; equity avg `0.0753` n `122`; fx avg `0.011` n `6`; index avg `0.0244` n `25`; metal avg `0.0053` n `20`; unknown avg `0.361` n `793`
- 4h: commodity avg `-0.0347` n `12`; crypto_alt avg `0.4111` n `231`; crypto_major avg `-0.4418` n `8`; equity avg `0.1827` n `122`; fx avg `0.0166` n `6`; index avg `0.0534` n `25`; metal avg `0.037` n `20`; unknown avg `0.8276` n `793`
- 24h: commodity avg `-0.0011` n `12`; crypto_alt avg `1.8576` n `231`; crypto_major avg `0.3599` n `8`; equity avg `0.7229` n `122`; fx avg `0.0423` n `6`; index avg `0.1053` n `25`; metal avg `0.0656` n `20`; unknown avg `5.2808` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
