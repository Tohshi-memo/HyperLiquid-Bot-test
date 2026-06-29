# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T12:52:29.481443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.5658` n `228`; crypto_major avg `-0.6595` n `8`; equity avg `-0.178` n `88`; fx avg `0.0099` n `6`; index avg `-0.0209` n `23`; metal avg `-0.0231` n `20`; unknown avg `0.1233` n `764`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `0.2166` n `228`; crypto_major avg `0.2961` n `8`; equity avg `-0.1235` n `88`; fx avg `0.038` n `6`; index avg `-0.0315` n `23`; metal avg `0.0604` n `20`; unknown avg `0.3499` n `764`
- 4h: commodity avg `-0.1159` n `12`; crypto_alt avg `0.165` n `228`; crypto_major avg `0.2971` n `8`; equity avg `0.0027` n `88`; fx avg `0.0684` n `6`; index avg `-0.0386` n `23`; metal avg `-0.1075` n `20`; unknown avg `-0.0257` n `764`
- 24h: commodity avg `-0.5713` n `12`; crypto_alt avg `0.1071` n `228`; crypto_major avg `-0.046` n `8`; equity avg `0.4358` n `88`; fx avg `0.1018` n `6`; index avg `0.0437` n `23`; metal avg `-0.373` n `20`; unknown avg `1.0906` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
