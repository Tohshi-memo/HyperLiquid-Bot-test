# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T08:22:28.727662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `13`; crypto_alt avg `-0.562` n `239`; crypto_major avg `-0.4678` n `8`; equity avg `-0.1622` n `162`; fx avg `-0.0037` n `6`; index avg `-0.0132` n `27`; metal avg `-0.0684` n `20`; unknown avg `0.1024` n `1250`
- 1h: commodity avg `-0.0425` n `13`; crypto_alt avg `-0.8388` n `239`; crypto_major avg `-0.8455` n `8`; equity avg `-0.3422` n `162`; fx avg `0.0109` n `6`; index avg `-0.0259` n `27`; metal avg `-0.1198` n `20`; unknown avg `0.3872` n `1194`
- 4h: commodity avg `-0.0397` n `13`; crypto_alt avg `1.2727` n `239`; crypto_major avg `0.3107` n `8`; equity avg `-0.3018` n `162`; fx avg `0.0583` n `6`; index avg `-0.0242` n `27`; metal avg `-0.2737` n `20`; unknown avg `0.4548` n `1166`
- 24h: commodity avg `0.4292` n `13`; crypto_alt avg `-1.3028` n `239`; crypto_major avg `-3.7152` n `8`; equity avg `-1.3348` n `162`; fx avg `-0.0328` n `6`; index avg `0.0163` n `27`; metal avg `-0.6392` n `20`; unknown avg `102.724` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
