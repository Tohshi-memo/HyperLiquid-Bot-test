# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T21:37:32.177414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.75` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `0.147` n `228`; crypto_major avg `0.1595` n `8`; equity avg `-0.0172` n `88`; fx avg `0.0123` n `6`; index avg `0.0012` n `23`; metal avg `0.0088` n `20`; unknown avg `1.0357` n `765`
- 1h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.0781` n `228`; crypto_major avg `0.0861` n `8`; equity avg `0.0837` n `88`; fx avg `0.0188` n `6`; index avg `0.032` n `23`; metal avg `0.0246` n `20`; unknown avg `1.8424` n `765`
- 4h: commodity avg `-0.1088` n `12`; crypto_alt avg `-0.5499` n `228`; crypto_major avg `0.1084` n `8`; equity avg `0.5017` n `88`; fx avg `0.0157` n `6`; index avg `0.0988` n `23`; metal avg `0.2702` n `20`; unknown avg `1.3018` n `765`
- 24h: commodity avg `-0.3667` n `12`; crypto_alt avg `1.8546` n `228`; crypto_major avg `3.0188` n `8`; equity avg `1.6703` n `88`; fx avg `0.209` n `6`; index avg `0.1531` n `23`; metal avg `-0.4872` n `20`; unknown avg `2.6735` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
