# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T16:07:27.528619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0209` n `12`; crypto_alt avg `-0.3593` n `231`; crypto_major avg `-0.1954` n `8`; equity avg `-0.0309` n `122`; fx avg `-0.007` n `6`; index avg `-0.0035` n `25`; metal avg `0.0034` n `20`; unknown avg `0.0195` n `793`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.0952` n `231`; crypto_major avg `-0.2798` n `8`; equity avg `0.0324` n `122`; fx avg `-0.005` n `6`; index avg `0.007` n `25`; metal avg `0.0299` n `20`; unknown avg `0.1264` n `793`
- 4h: commodity avg `-0.0289` n `12`; crypto_alt avg `1.7381` n `231`; crypto_major avg `0.3996` n `8`; equity avg `0.1544` n `122`; fx avg `-0.0079` n `6`; index avg `0.018` n `25`; metal avg `0.0404` n `20`; unknown avg `1.977` n `793`
- 24h: commodity avg `0.0125` n `12`; crypto_alt avg `2.4597` n `231`; crypto_major avg `1.4775` n `8`; equity avg `0.6436` n `122`; fx avg `0.0341` n `6`; index avg `0.0632` n `25`; metal avg `0.0755` n `20`; unknown avg `8.3932` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
