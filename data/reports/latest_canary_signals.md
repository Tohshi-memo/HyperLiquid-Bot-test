# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T17:02:52.173453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.2612` n `231`; crypto_major avg `-0.24` n `8`; equity avg `-0.0363` n `122`; fx avg `0.0075` n `6`; index avg `0.0033` n `25`; metal avg `-0.0461` n `20`; unknown avg `-0.1856` n `795`
- 1h: commodity avg `0.0317` n `12`; crypto_alt avg `-0.2387` n `231`; crypto_major avg `-0.2688` n `8`; equity avg `-0.1988` n `122`; fx avg `-0.004` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0443` n `20`; unknown avg `-0.1667` n `795`
- 4h: commodity avg `0.1208` n `12`; crypto_alt avg `-0.4168` n `231`; crypto_major avg `-0.0772` n `8`; equity avg `0.3812` n `122`; fx avg `-0.0026` n `6`; index avg `-0.0292` n `25`; metal avg `0.2463` n `20`; unknown avg `-0.1309` n `795`
- 24h: commodity avg `-0.5563` n `12`; crypto_alt avg `-1.0808` n `231`; crypto_major avg `-0.0214` n `8`; equity avg `1.4054` n `122`; fx avg `0.0463` n `6`; index avg `0.1834` n `25`; metal avg `-0.1535` n `20`; unknown avg `-0.8199` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
