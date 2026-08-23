# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T22:57:13.830427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.0144` n `231`; crypto_major avg `0.0044` n `8`; equity avg `0.0231` n `122`; fx avg `-0.0045` n `6`; index avg `0.0351` n `25`; metal avg `-0.0563` n `20`; unknown avg `-0.082` n `793`
- 1h: commodity avg `-0.0541` n `12`; crypto_alt avg `-0.3857` n `231`; crypto_major avg `-0.1929` n `8`; equity avg `-0.0647` n `122`; fx avg `0.0145` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0623` n `20`; unknown avg `-0.1442` n `793`
- 4h: commodity avg `-0.0881` n `12`; crypto_alt avg `0.2583` n `231`; crypto_major avg `0.6505` n `8`; equity avg `0.0119` n `122`; fx avg `-0.0893` n `6`; index avg `-0.005` n `25`; metal avg `-0.0491` n `20`; unknown avg `0.7647` n `793`
- 24h: commodity avg `-0.2232` n `12`; crypto_alt avg `3.6411` n `231`; crypto_major avg `1.9505` n `8`; equity avg `0.7339` n `122`; fx avg `-0.0952` n `6`; index avg `0.1202` n `25`; metal avg `0.0513` n `20`; unknown avg `5.5927` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
