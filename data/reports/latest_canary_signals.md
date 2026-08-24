# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T05:52:21.874056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `12`; crypto_alt avg `0.0789` n `231`; crypto_major avg `0.035` n `8`; equity avg `-0.0147` n `122`; fx avg `0.0267` n `6`; index avg `-0.0024` n `25`; metal avg `0.0605` n `20`; unknown avg `0.1443` n `793`
- 1h: commodity avg `0.0144` n `12`; crypto_alt avg `0.2864` n `231`; crypto_major avg `0.2413` n `8`; equity avg `-0.2218` n `122`; fx avg `-0.0016` n `6`; index avg `-0.0379` n `25`; metal avg `0.0159` n `20`; unknown avg `-0.2096` n `793`
- 4h: commodity avg `0.1093` n `12`; crypto_alt avg `0.2936` n `231`; crypto_major avg `-0.0139` n `8`; equity avg `-1.091` n `122`; fx avg `-0.0317` n `6`; index avg `-0.1435` n `25`; metal avg `0.076` n `20`; unknown avg `0.6989` n `793`
- 24h: commodity avg `-0.263` n `12`; crypto_alt avg `4.535` n `231`; crypto_major avg `1.7724` n `8`; equity avg `-1.1472` n `122`; fx avg `-0.1798` n `6`; index avg `-0.1198` n `25`; metal avg `0.1283` n `20`; unknown avg `5.8169` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
