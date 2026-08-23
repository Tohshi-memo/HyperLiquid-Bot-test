# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T20:19:59.666941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `0.1984` n `231`; crypto_major avg `0.2018` n `8`; equity avg `-0.0022` n `122`; fx avg `-0.02` n `6`; index avg `-0.004` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0041` n `793`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.0525` n `231`; crypto_major avg `0.066` n `8`; equity avg `-0.0232` n `122`; fx avg `-0.0564` n `6`; index avg `-0.0046` n `25`; metal avg `0.0082` n `20`; unknown avg `0.4922` n `793`
- 4h: commodity avg `-0.0324` n `12`; crypto_alt avg `0.5298` n `231`; crypto_major avg `0.3577` n `8`; equity avg `0.263` n `122`; fx avg `-0.0559` n `6`; index avg `0.0527` n `25`; metal avg `0.0147` n `20`; unknown avg `0.8836` n `793`
- 24h: commodity avg `-0.0921` n `12`; crypto_alt avg `2.3018` n `231`; crypto_major avg `0.1138` n `8`; equity avg `0.7303` n `122`; fx avg `-0.0519` n `6`; index avg `0.1265` n `25`; metal avg `0.0897` n `20`; unknown avg `5.5756` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
