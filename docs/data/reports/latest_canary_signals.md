# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T10:52:32.284513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0309` n `13`; crypto_alt avg `-0.214` n `236`; crypto_major avg `-0.2042` n `8`; equity avg `-0.2568` n `151`; fx avg `0.0124` n `6`; index avg `-0.0349` n `26`; metal avg `0.0073` n `20`; unknown avg `-0.1461` n `1136`
- 1h: commodity avg `0.1095` n `13`; crypto_alt avg `-0.6034` n `236`; crypto_major avg `-0.616` n `8`; equity avg `-0.3742` n `151`; fx avg `-0.0068` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0425` n `20`; unknown avg `-0.2712` n `1062`
- 4h: commodity avg `0.0421` n `13`; crypto_alt avg `0.0315` n `236`; crypto_major avg `0.0661` n `8`; equity avg `-0.4803` n `151`; fx avg `0.0303` n `6`; index avg `0.0009` n `26`; metal avg `0.2564` n `20`; unknown avg `4.3052` n `1038`
- 24h: commodity avg `-0.3701` n `13`; crypto_alt avg `-4.7804` n `236`; crypto_major avg `-3.6393` n `8`; equity avg `-6.1396` n `151`; fx avg `0.0617` n `6`; index avg `-0.9651` n `26`; metal avg `-0.3927` n `20`; unknown avg `2.2007` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1217`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0865`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
