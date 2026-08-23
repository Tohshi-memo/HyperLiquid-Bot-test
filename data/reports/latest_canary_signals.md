# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T20:52:21.947178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0534` n `231`; crypto_major avg `0.0076` n `8`; equity avg `-0.0031` n `122`; fx avg `-0.002` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.096` n `793`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.0954` n `231`; crypto_major avg `-0.0126` n `8`; equity avg `-0.0108` n `122`; fx avg `-0.0167` n `6`; index avg `-0.0091` n `25`; metal avg `0.0321` n `20`; unknown avg `1.2463` n `793`
- 4h: commodity avg `-0.0371` n `12`; crypto_alt avg `0.0694` n `231`; crypto_major avg `0.0028` n `8`; equity avg `0.1988` n `122`; fx avg `-0.0821` n `6`; index avg `0.0423` n `25`; metal avg `0.03` n `20`; unknown avg `1.861` n `793`
- 24h: commodity avg `-0.0772` n `12`; crypto_alt avg `2.1136` n `231`; crypto_major avg `0.0256` n `8`; equity avg `0.7404` n `122`; fx avg `-0.0785` n `6`; index avg `0.1258` n `25`; metal avg `0.1219` n `20`; unknown avg `5.6389` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
