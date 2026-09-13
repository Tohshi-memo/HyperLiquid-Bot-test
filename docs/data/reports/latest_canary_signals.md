# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T23:28:24.992219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0489` n `12`; crypto_alt avg `0.0339` n `233`; crypto_major avg `-0.0266` n `8`; equity avg `-0.0617` n `136`; fx avg `-0.0028` n `6`; index avg `0.0003` n `27`; metal avg `-0.0294` n `20`; unknown avg `8.7249` n `840`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-0.1122` n `233`; crypto_major avg `-0.0216` n `8`; equity avg `-0.1114` n `136`; fx avg `-0.0068` n `6`; index avg `0.0361` n `27`; metal avg `0.0559` n `20`; unknown avg `8.1573` n `838`
- 4h: commodity avg `0.358` n `12`; crypto_alt avg `-1.6554` n `233`; crypto_major avg `-1.011` n `8`; equity avg `-0.4267` n `136`; fx avg `0.0292` n `6`; index avg `-0.0386` n `27`; metal avg `-0.0634` n `20`; unknown avg `14.3339` n `802`
- 24h: commodity avg `0.6746` n `12`; crypto_alt avg `-1.6158` n `233`; crypto_major avg `-1.7017` n `8`; equity avg `-1.5408` n `136`; fx avg `0.0467` n `6`; index avg `-0.2816` n `26`; metal avg `-0.1233` n `20`; unknown avg `2.6626` n `716`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
