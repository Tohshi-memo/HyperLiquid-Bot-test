# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T18:52:29.600175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `0.0737` n `231`; crypto_major avg `0.0056` n `8`; equity avg `0.0574` n `122`; fx avg `0.0028` n `6`; index avg `0.0323` n `25`; metal avg `0.019` n `20`; unknown avg `-0.0377` n `797`
- 1h: commodity avg `-0.1517` n `12`; crypto_alt avg `0.3053` n `231`; crypto_major avg `0.0646` n `8`; equity avg `0.1289` n `122`; fx avg `-0.0056` n `6`; index avg `0.0286` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.0641` n `797`
- 4h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.3822` n `231`; crypto_major avg `0.4644` n `8`; equity avg `0.2704` n `122`; fx avg `0.0048` n `6`; index avg `0.0304` n `25`; metal avg `-0.0961` n `20`; unknown avg `0.1368` n `797`
- 24h: commodity avg `0.0621` n `12`; crypto_alt avg `-1.7705` n `231`; crypto_major avg `-1.7628` n `8`; equity avg `-0.1786` n `122`; fx avg `-0.0563` n `6`; index avg `0.0356` n `25`; metal avg `-0.304` n `20`; unknown avg `0.4674` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
