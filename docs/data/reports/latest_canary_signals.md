# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T16:22:35.402114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.163` n `234`; crypto_major avg `-0.0003` n `8`; equity avg `-0.0103` n `141`; fx avg `0.0036` n `6`; index avg `0.0045` n `26`; metal avg `0.002` n `20`; unknown avg `0.5458` n `962`
- 1h: commodity avg `-0.0641` n `12`; crypto_alt avg `0.6037` n `234`; crypto_major avg `0.1619` n `8`; equity avg `0.0421` n `141`; fx avg `0.0143` n `6`; index avg `0.0161` n `26`; metal avg `0.0049` n `20`; unknown avg `1.0291` n `954`
- 4h: commodity avg `-0.1703` n `12`; crypto_alt avg `-0.8149` n `234`; crypto_major avg `-0.9641` n `8`; equity avg `-0.0616` n `141`; fx avg `0.0162` n `6`; index avg `0.0047` n `26`; metal avg `-0.0084` n `20`; unknown avg `5.4197` n `954`
- 24h: commodity avg `-0.1216` n `12`; crypto_alt avg `-1.0674` n `234`; crypto_major avg `-0.2734` n `8`; equity avg `0.2086` n `141`; fx avg `-0.012` n `6`; index avg `0.0171` n `26`; metal avg `-0.0092` n `20`; unknown avg `28.072` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
