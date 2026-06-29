# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T13:37:27.656919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0243` n `12`; crypto_alt avg `-0.4035` n `228`; crypto_major avg `-0.3696` n `8`; equity avg `-0.2144` n `88`; fx avg `0.0139` n `6`; index avg `-0.0429` n `23`; metal avg `-0.1108` n `20`; unknown avg `0.412` n `764`
- 1h: commodity avg `0.0064` n `12`; crypto_alt avg `-0.6633` n `228`; crypto_major avg `-0.4413` n `8`; equity avg `-0.2727` n `88`; fx avg `0.006` n `6`; index avg `-0.0565` n `23`; metal avg `-0.1373` n `20`; unknown avg `0.4843` n `764`
- 4h: commodity avg `-0.183` n `12`; crypto_alt avg `0.0446` n `228`; crypto_major avg `0.5866` n `8`; equity avg `-0.0521` n `88`; fx avg `0.062` n `6`; index avg `-0.0533` n `23`; metal avg `-0.094` n `20`; unknown avg `0.8956` n `764`
- 24h: commodity avg `-0.6062` n `12`; crypto_alt avg `0.1669` n `228`; crypto_major avg `0.2509` n `8`; equity avg `0.3396` n `88`; fx avg `0.103` n `6`; index avg `0.0031` n `23`; metal avg `-0.4603` n `20`; unknown avg `1.5366` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
