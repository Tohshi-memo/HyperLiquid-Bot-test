# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T23:07:26.090397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.1009` n `230`; crypto_major avg `0.0793` n `8`; equity avg `-0.0125` n `114`; fx avg `0.0028` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0125` n `20`; unknown avg `0.0626` n `791`
- 1h: commodity avg `-0.0677` n `12`; crypto_alt avg `0.1904` n `230`; crypto_major avg `-0.0201` n `8`; equity avg `-0.0186` n `114`; fx avg `0.0206` n `6`; index avg `-0.0036` n `25`; metal avg `0.1184` n `20`; unknown avg `-0.0203` n `791`
- 4h: commodity avg `-0.1289` n `12`; crypto_alt avg `-0.7469` n `230`; crypto_major avg `-0.5782` n `8`; equity avg `-0.0249` n `114`; fx avg `-0.0062` n `6`; index avg `0.0151` n `25`; metal avg `0.0347` n `20`; unknown avg `0.7183` n `791`
- 24h: commodity avg `-0.0573` n `12`; crypto_alt avg `-0.8349` n `230`; crypto_major avg `-0.5045` n `8`; equity avg `0.2489` n `114`; fx avg `-0.0096` n `6`; index avg `0.0437` n `25`; metal avg `0.0947` n `20`; unknown avg `-0.0058` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
