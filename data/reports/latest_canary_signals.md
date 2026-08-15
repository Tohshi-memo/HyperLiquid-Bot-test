# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T15:37:32.222694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.1179` n `230`; crypto_major avg `0.1103` n `8`; equity avg `-0.0001` n `114`; fx avg `-0.0006` n `6`; index avg `0.0028` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0057` n `791`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.3034` n `230`; crypto_major avg `0.1769` n `8`; equity avg `0.0254` n `114`; fx avg `0.0012` n `6`; index avg `0.0096` n `25`; metal avg `-0.0019` n `20`; unknown avg `5.1111` n `791`
- 4h: commodity avg `-0.0468` n `12`; crypto_alt avg `0.4035` n `230`; crypto_major avg `0.2719` n `8`; equity avg `0.0773` n `114`; fx avg `-0.0038` n `6`; index avg `0.0225` n `25`; metal avg `-0.0161` n `20`; unknown avg `-0.0572` n `791`
- 24h: commodity avg `-0.1146` n `12`; crypto_alt avg `1.3857` n `230`; crypto_major avg `0.2902` n `8`; equity avg `0.3673` n `114`; fx avg `0.0315` n `6`; index avg `0.043` n `25`; metal avg `0.0259` n `20`; unknown avg `-0.0248` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
