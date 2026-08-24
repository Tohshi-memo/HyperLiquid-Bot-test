# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T00:07:25.795043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `-0.6254` n `231`; crypto_major avg `-0.3208` n `8`; equity avg `-0.1983` n `122`; fx avg `-0.0311` n `6`; index avg `-0.0231` n `25`; metal avg `0.1196` n `20`; unknown avg `0.1439` n `793`
- 1h: commodity avg `0.0102` n `12`; crypto_alt avg `-0.5612` n `231`; crypto_major avg `-0.136` n `8`; equity avg `-0.0407` n `122`; fx avg `-0.0188` n `6`; index avg `0.0033` n `25`; metal avg `0.1989` n `20`; unknown avg `0.1674` n `793`
- 4h: commodity avg `-0.1177` n `12`; crypto_alt avg `-0.2654` n `231`; crypto_major avg `0.5078` n `8`; equity avg `-0.0554` n `122`; fx avg `-0.0704` n `6`; index avg `-0.0207` n `25`; metal avg `0.1583` n `20`; unknown avg `0.6404` n `793`
- 24h: commodity avg `-0.225` n `12`; crypto_alt avg `2.7483` n `231`; crypto_major avg `1.2315` n `8`; equity avg `0.6217` n `122`; fx avg `-0.1522` n `6`; index avg `0.0984` n `25`; metal avg `0.2405` n `20`; unknown avg `5.7753` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
