# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T17:22:33.084443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.2327` n `228`; crypto_major avg `-0.2717` n `8`; equity avg `-0.0881` n `88`; fx avg `-0.004` n `6`; index avg `-0.0044` n `23`; metal avg `0.0078` n `20`; unknown avg `-0.0936` n `765`
- 1h: commodity avg `-0.1099` n `12`; crypto_alt avg `0.1491` n `228`; crypto_major avg `0.3338` n `8`; equity avg `0.1303` n `88`; fx avg `-0.0129` n `6`; index avg `0.0256` n `23`; metal avg `-0.1148` n `20`; unknown avg `0.2067` n `765`
- 4h: commodity avg `-0.1514` n `12`; crypto_alt avg `0.6195` n `228`; crypto_major avg `0.4708` n `8`; equity avg `1.2234` n `88`; fx avg `0.0563` n `6`; index avg `0.2608` n `23`; metal avg `-0.0531` n `20`; unknown avg `0.0705` n `765`
- 24h: commodity avg `0.0236` n `12`; crypto_alt avg `-2.5598` n `228`; crypto_major avg `-2.4818` n `8`; equity avg `1.368` n `88`; fx avg `0.1286` n `6`; index avg `0.3803` n `23`; metal avg `0.3554` n `20`; unknown avg `8.6786` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
