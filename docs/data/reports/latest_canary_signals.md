# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T07:22:26.198846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `0.4563` n `239`; crypto_major avg `0.4208` n `8`; equity avg `0.0335` n `161`; fx avg `0.0209` n `6`; index avg `-0.0009` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.2079` n `1261`
- 1h: commodity avg `-0.0996` n `13`; crypto_alt avg `-0.1063` n `239`; crypto_major avg `-0.1577` n `8`; equity avg `-0.1314` n `161`; fx avg `0.0121` n `6`; index avg `-0.023` n `27`; metal avg `0.0168` n `20`; unknown avg `7.9263` n `1249`
- 4h: commodity avg `-0.0564` n `13`; crypto_alt avg `-0.9297` n `239`; crypto_major avg `-0.3891` n `8`; equity avg `0.5243` n `161`; fx avg `-0.0246` n `6`; index avg `0.0624` n `27`; metal avg `0.1804` n `20`; unknown avg `-0.0325` n `1213`
- 24h: commodity avg `0.2968` n `13`; crypto_alt avg `-1.2618` n `239`; crypto_major avg `-2.4772` n `8`; equity avg `1.759` n `161`; fx avg `-0.1849` n `6`; index avg `0.2064` n `27`; metal avg `0.0386` n `20`; unknown avg `1.4475` n `1160`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
