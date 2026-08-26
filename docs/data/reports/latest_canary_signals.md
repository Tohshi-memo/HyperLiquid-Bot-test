# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T13:22:31.791799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `-0.3128` n `231`; crypto_major avg `-0.3356` n `8`; equity avg `0.0011` n `122`; fx avg `0.0068` n `6`; index avg `0.0058` n `25`; metal avg `-0.0199` n `20`; unknown avg `-0.0847` n `797`
- 1h: commodity avg `0.0455` n `12`; crypto_alt avg `-0.684` n `231`; crypto_major avg `-0.9316` n `8`; equity avg `-0.4408` n `122`; fx avg `-0.0011` n `6`; index avg `-0.0542` n `25`; metal avg `-0.0992` n `20`; unknown avg `-0.0581` n `797`
- 4h: commodity avg `0.2067` n `12`; crypto_alt avg `-0.2036` n `231`; crypto_major avg `-0.3747` n `8`; equity avg `-0.4664` n `122`; fx avg `0.0015` n `6`; index avg `-0.0397` n `25`; metal avg `-0.1045` n `20`; unknown avg `-0.0663` n `797`
- 24h: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.9498` n `231`; crypto_major avg `-0.9043` n `8`; equity avg `-0.2291` n `122`; fx avg `-0.0601` n `6`; index avg `-0.0627` n `25`; metal avg `0.2123` n `20`; unknown avg `0.6894` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
