# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T06:07:26.611217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0817` n `12`; crypto_alt avg `-0.1306` n `229`; crypto_major avg `-0.1481` n `8`; equity avg `-0.0495` n `91`; fx avg `0.0271` n `6`; index avg `0.0117` n `25`; metal avg `0.0984` n `20`; unknown avg `0.0344` n `745`
- 1h: commodity avg `0.1668` n `12`; crypto_alt avg `0.1964` n `229`; crypto_major avg `0.224` n `8`; equity avg `0.6678` n `91`; fx avg `0.0131` n `6`; index avg `0.1246` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.1331` n `745`
- 4h: commodity avg `0.0701` n `12`; crypto_alt avg `-0.9525` n `229`; crypto_major avg `-1.0247` n `8`; equity avg `-0.5478` n `91`; fx avg `-0.0143` n `6`; index avg `-0.1261` n `25`; metal avg `-0.2991` n `20`; unknown avg `14.5654` n `745`
- 24h: commodity avg `0.1782` n `12`; crypto_alt avg `0.3503` n `229`; crypto_major avg `-0.5347` n `8`; equity avg `-1.3974` n `90`; fx avg `0.0124` n `6`; index avg `-0.3003` n `25`; metal avg `-0.335` n `20`; unknown avg `-0.3703` n `743`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
