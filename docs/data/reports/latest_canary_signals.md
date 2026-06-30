# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T02:22:25.999127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2639` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.0961` n `228`; crypto_major avg `-0.0704` n `8`; equity avg `0.0746` n `88`; fx avg `-0.0102` n `6`; index avg `0.0138` n `23`; metal avg `-0.12` n `20`; unknown avg `-0.2455` n `765`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `-0.0393` n `228`; crypto_major avg `-0.1121` n `8`; equity avg `0.2626` n `88`; fx avg `-0.0158` n `6`; index avg `0.0644` n `23`; metal avg `-0.0658` n `20`; unknown avg `-0.2567` n `763`
- 4h: commodity avg `0.0072` n `12`; crypto_alt avg `-1.0255` n `228`; crypto_major avg `-1.2955` n `8`; equity avg `-0.1432` n `88`; fx avg `0.0447` n `6`; index avg `-0.0316` n `23`; metal avg `-0.5579` n `20`; unknown avg `0.3145` n `763`
- 24h: commodity avg `-0.2571` n `12`; crypto_alt avg `0.7271` n `228`; crypto_major avg `1.9047` n `8`; equity avg `2.2145` n `88`; fx avg `0.1621` n `6`; index avg `0.2893` n `23`; metal avg `-0.8673` n `20`; unknown avg `1.6952` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
