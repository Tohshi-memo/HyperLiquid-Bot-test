# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T02:16:48.984540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.0715` n `234`; crypto_major avg `0.0074` n `8`; equity avg `0.1351` n `141`; fx avg `-0.0027` n `6`; index avg `0.0122` n `26`; metal avg `0.0377` n `20`; unknown avg `0.0212` n `963`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.7709` n `234`; crypto_major avg `-0.2389` n `8`; equity avg `0.1914` n `141`; fx avg `0.0013` n `6`; index avg `0.0309` n `26`; metal avg `0.0379` n `20`; unknown avg `0.1154` n `961`
- 4h: commodity avg `0.0464` n `12`; crypto_alt avg `-0.7476` n `234`; crypto_major avg `-0.3691` n `8`; equity avg `-0.2856` n `141`; fx avg `-0.0219` n `6`; index avg `-0.054` n `26`; metal avg `-0.0395` n `20`; unknown avg `0.0573` n `955`
- 24h: commodity avg `0.0264` n `12`; crypto_alt avg `-4.2726` n `234`; crypto_major avg `-1.9501` n `8`; equity avg `-2.1903` n `141`; fx avg `-0.0611` n `6`; index avg `-0.181` n `26`; metal avg `-0.5882` n `20`; unknown avg `135.2246` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
