# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T09:41:17.280892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0667` n `13`; crypto_alt avg `-0.194` n `237`; crypto_major avg `-0.1677` n `8`; equity avg `-0.0528` n `151`; fx avg `0.009` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0277` n `20`; unknown avg `-0.0263` n `1198`
- 1h: commodity avg `0.1049` n `13`; crypto_alt avg `-0.3014` n `237`; crypto_major avg `-0.207` n `8`; equity avg `-0.4984` n `151`; fx avg `-0.0101` n `6`; index avg `-0.1014` n `26`; metal avg `-0.0908` n `20`; unknown avg `-0.2664` n `1196`
- 4h: commodity avg `0.3083` n `13`; crypto_alt avg `-0.5609` n `237`; crypto_major avg `-0.494` n `8`; equity avg `-0.2312` n `151`; fx avg `-0.0086` n `6`; index avg `-0.0205` n `26`; metal avg `-0.047` n `20`; unknown avg `3.816` n `1160`
- 24h: commodity avg `0.3417` n `13`; crypto_alt avg `-0.7948` n `237`; crypto_major avg `-1.4604` n `8`; equity avg `-1.7897` n `151`; fx avg `-0.0003` n `6`; index avg `-0.2685` n `26`; metal avg `-0.263` n `20`; unknown avg `4.0707` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
