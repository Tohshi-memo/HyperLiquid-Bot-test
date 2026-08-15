# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T15:22:32.712809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `0.0091` n `230`; crypto_major avg `0.0129` n `8`; equity avg `0.016` n `114`; fx avg `0.0006` n `6`; index avg `0.0008` n `25`; metal avg `0.0014` n `20`; unknown avg `5.6231` n `791`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.2034` n `230`; crypto_major avg `0.0969` n `8`; equity avg `0.0364` n `114`; fx avg `0.002` n `6`; index avg `0.0014` n `25`; metal avg `-0.0003` n `20`; unknown avg `5.1037` n `791`
- 4h: commodity avg `0.0032` n `12`; crypto_alt avg `0.2781` n `230`; crypto_major avg `0.1402` n `8`; equity avg `0.062` n `114`; fx avg `-0.0044` n `6`; index avg `0.0206` n `25`; metal avg `-0.0193` n `20`; unknown avg `-0.0575` n `791`
- 24h: commodity avg `-0.1155` n `12`; crypto_alt avg `1.6034` n `230`; crypto_major avg `0.4961` n `8`; equity avg `0.2799` n `114`; fx avg `0.0551` n `6`; index avg `0.014` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.0239` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
