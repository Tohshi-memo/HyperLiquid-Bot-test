# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T11:22:30.591796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.025` n `13`; crypto_alt avg `0.0263` n `235`; crypto_major avg `-0.012` n `8`; equity avg `0.0868` n `150`; fx avg `0.0052` n `6`; index avg `0.0084` n `26`; metal avg `0.0688` n `20`; unknown avg `2.3846` n `1078`
- 1h: commodity avg `0.006` n `13`; crypto_alt avg `-0.5484` n `235`; crypto_major avg `-0.3331` n `8`; equity avg `-0.0002` n `150`; fx avg `-0.03` n `6`; index avg `-0.009` n `26`; metal avg `0.0364` n `20`; unknown avg `1.6447` n `1076`
- 4h: commodity avg `-0.1361` n `13`; crypto_alt avg `-0.8208` n `235`; crypto_major avg `-0.4712` n `8`; equity avg `-0.0431` n `150`; fx avg `-0.0616` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0399` n `20`; unknown avg `0.3583` n `1006`
- 24h: commodity avg `-0.546` n `13`; crypto_alt avg `-1.5049` n `235`; crypto_major avg `-1.5406` n `8`; equity avg `-0.0593` n `150`; fx avg `0.0351` n `6`; index avg `0.0891` n `26`; metal avg `0.5586` n `20`; unknown avg `7.5814` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
