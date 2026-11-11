# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T11:52:34.380015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0265` n `13`; crypto_alt avg `0.2851` n `239`; crypto_major avg `0.13` n `8`; equity avg `-0.1183` n `161`; fx avg `0.0039` n `6`; index avg `-0.0095` n `27`; metal avg `-0.0575` n `20`; unknown avg `0.1825` n `1261`
- 1h: commodity avg `-0.0588` n `13`; crypto_alt avg `0.1116` n `239`; crypto_major avg `-0.058` n `8`; equity avg `-0.0481` n `161`; fx avg `-0.0328` n `6`; index avg `0.0062` n `27`; metal avg `-0.1` n `20`; unknown avg `159.3197` n `1255`
- 4h: commodity avg `0.2133` n `13`; crypto_alt avg `0.557` n `239`; crypto_major avg `0.3771` n `8`; equity avg `0.7546` n `161`; fx avg `-0.0379` n `6`; index avg `0.0344` n `27`; metal avg `0.0215` n `20`; unknown avg `41.0721` n `1223`
- 24h: commodity avg `0.6915` n `13`; crypto_alt avg `-0.3449` n `239`; crypto_major avg `-1.1549` n `8`; equity avg `2.8467` n `161`; fx avg `-0.2084` n `6`; index avg `0.2743` n `27`; metal avg `0.2676` n `20`; unknown avg `1.3133` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
