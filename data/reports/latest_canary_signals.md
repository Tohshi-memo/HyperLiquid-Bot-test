# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T05:37:25.349453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1658` n `231`; crypto_major avg `-0.1671` n `8`; equity avg `-0.1537` n `122`; fx avg `-0.0192` n `6`; index avg `-0.0415` n `25`; metal avg `-0.0431` n `20`; unknown avg `-0.086` n `793`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.1845` n `231`; crypto_major avg `-0.2486` n `8`; equity avg `-0.2224` n `122`; fx avg `-0.0416` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0337` n `20`; unknown avg `0.1` n `793`
- 4h: commodity avg `0.1003` n `12`; crypto_alt avg `0.0091` n `231`; crypto_major avg `-0.1681` n `8`; equity avg `-1.245` n `122`; fx avg `-0.0743` n `6`; index avg `-0.1563` n `25`; metal avg `0.0574` n `20`; unknown avg `-0.4407` n `793`
- 24h: commodity avg `-0.2708` n `12`; crypto_alt avg `4.2071` n `231`; crypto_major avg `1.4217` n `8`; equity avg `-1.1787` n `122`; fx avg `-0.2181` n `6`; index avg `-0.1205` n `25`; metal avg `0.0683` n `20`; unknown avg `5.8952` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
