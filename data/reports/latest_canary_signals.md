# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T12:37:26.965607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0786` n `12`; crypto_alt avg `-0.1821` n `228`; crypto_major avg `-0.2686` n `8`; equity avg `-0.14` n `88`; fx avg `0.0214` n `6`; index avg `-0.0104` n `23`; metal avg `0.0564` n `20`; unknown avg `0.055` n `764`
- 1h: commodity avg `-0.1229` n `12`; crypto_alt avg `0.6663` n `228`; crypto_major avg `0.8449` n `8`; equity avg `0.0737` n `88`; fx avg `0.0364` n `6`; index avg `-0.0133` n `23`; metal avg `0.1694` n `20`; unknown avg `0.2811` n `764`
- 4h: commodity avg `-0.0976` n `12`; crypto_alt avg `0.7845` n `228`; crypto_major avg `1.0458` n `8`; equity avg `0.1616` n `88`; fx avg `0.0484` n `6`; index avg `-0.014` n `23`; metal avg `-0.1786` n `20`; unknown avg `-0.051` n `764`
- 24h: commodity avg `-0.5515` n `12`; crypto_alt avg `0.6041` n `228`; crypto_major avg `0.6276` n `8`; equity avg `0.6372` n `88`; fx avg `0.0919` n `6`; index avg `0.0678` n `23`; metal avg `-0.3541` n `20`; unknown avg `1.0294` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
