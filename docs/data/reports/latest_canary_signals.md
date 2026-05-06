# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T23:50:59.343063+00:00`
- Correlation status: `ready`
- Asset price records: `499`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0404` n `12`; crypto_alt avg `0.0913` n `228`; crypto_major avg `0.0063` n `8`; equity avg `-0.0639` n `65`; fx avg `-0.0005` n `4`; index avg `0.044` n `23`; metal avg `0.115` n `18`; unknown avg `0.0592` n `356`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `0.1153` n `228`; crypto_major avg `0.0198` n `8`; equity avg `0.159` n `65`; fx avg `0.0157` n `4`; index avg `0.1119` n `23`; metal avg `0.0753` n `18`; unknown avg `0.1183` n `356`
- 4h: commodity avg `0.3241` n `12`; crypto_alt avg `0.3018` n `228`; crypto_major avg `-0.2641` n `8`; equity avg `-0.1104` n `65`; fx avg `0.0073` n `4`; index avg `-0.0134` n `23`; metal avg `0.0667` n `18`; unknown avg `0.1678` n `356`
- 24h: commodity avg `-1.5702` n `7`; crypto_alt avg `2.4211` n `223`; crypto_major avg `0.4229` n `7`; equity avg `2.0296` n `47`; fx avg `-0.6186` n `4`; index avg `1.6065` n `6`; metal avg `2.792` n `7`; unknown avg `4.0949` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1305`, n `495`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `495`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1036`, n `491`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0926`, n `491`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0866`, n `491`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `491`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0775`, n `491`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `495`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0638`, n `491`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0596`, n `491`, weak_sample_signal
