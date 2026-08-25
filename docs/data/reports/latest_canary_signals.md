# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T16:07:46.845852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `0.2538` n `231`; crypto_major avg `0.1368` n `8`; equity avg `0.1457` n `122`; fx avg `-0.0` n `6`; index avg `0.0188` n `25`; metal avg `0.0189` n `20`; unknown avg `0.0455` n `795`
- 1h: commodity avg `-0.0528` n `12`; crypto_alt avg `0.1942` n `231`; crypto_major avg `0.2367` n `8`; equity avg `0.3232` n `122`; fx avg `-0.0079` n `6`; index avg `0.0565` n `25`; metal avg `0.1392` n `20`; unknown avg `0.0832` n `795`
- 4h: commodity avg `0.0496` n `12`; crypto_alt avg `0.2082` n `231`; crypto_major avg `0.478` n `8`; equity avg `0.4944` n `122`; fx avg `0.0296` n `6`; index avg `-0.0575` n `25`; metal avg `0.1846` n `20`; unknown avg `0.0986` n `795`
- 24h: commodity avg `-0.6263` n `12`; crypto_alt avg `-1.424` n `231`; crypto_major avg `-0.5014` n `8`; equity avg `1.6417` n `122`; fx avg `0.041` n `6`; index avg `0.1924` n `25`; metal avg `-0.1544` n `20`; unknown avg `-0.6604` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
