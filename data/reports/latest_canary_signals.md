# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T13:07:27.741451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.136` n `12`; crypto_alt avg `-0.1983` n `231`; crypto_major avg `-0.3028` n `8`; equity avg `-0.0603` n `122`; fx avg `-0.0061` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0647` n `20`; unknown avg `-0.0864` n `797`
- 1h: commodity avg `0.0941` n `12`; crypto_alt avg `-0.0714` n `231`; crypto_major avg `-0.1873` n `8`; equity avg `-0.4313` n `122`; fx avg `-0.0135` n `6`; index avg `-0.0486` n `25`; metal avg `-0.1083` n `20`; unknown avg `0.0039` n `797`
- 4h: commodity avg `0.2564` n `12`; crypto_alt avg `-0.4479` n `231`; crypto_major avg `-0.5746` n `8`; equity avg `-0.5049` n `122`; fx avg `-0.0113` n `6`; index avg `-0.052` n `25`; metal avg `-0.1129` n `20`; unknown avg `-0.1166` n `797`
- 24h: commodity avg `0.0604` n `12`; crypto_alt avg `-1.5068` n `231`; crypto_major avg `-1.3825` n `8`; equity avg `-0.182` n `122`; fx avg `-0.0443` n `6`; index avg `-0.0646` n `25`; metal avg `0.1627` n `20`; unknown avg `0.6343` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
