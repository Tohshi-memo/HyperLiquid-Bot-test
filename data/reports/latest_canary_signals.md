# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T20:07:28.213320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.9199` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8624` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0482` n `12`; crypto_alt avg `0.3261` n `234`; crypto_major avg `0.2826` n `8`; equity avg `0.2052` n `137`; fx avg `0.027` n `6`; index avg `0.0254` n `27`; metal avg `0.0297` n `20`; unknown avg `88.792` n `903`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.0475` n `234`; crypto_major avg `0.2951` n `8`; equity avg `0.4047` n `137`; fx avg `0.0628` n `6`; index avg `0.0497` n `27`; metal avg `0.0266` n `20`; unknown avg `16.5177` n `895`
- 4h: commodity avg `-0.033` n `12`; crypto_alt avg `1.3249` n `234`; crypto_major avg `1.3156` n `8`; equity avg `-0.6043` n `137`; fx avg `0.0626` n `6`; index avg `-0.2172` n `27`; metal avg `-0.5468` n `20`; unknown avg `2.2093` n `857`
- 24h: commodity avg `-0.6718` n `12`; crypto_alt avg `-0.3178` n `234`; crypto_major avg `0.8822` n `8`; equity avg `0.6635` n `137`; fx avg `0.0914` n `6`; index avg `0.0121` n `27`; metal avg `-0.2731` n `20`; unknown avg `0.816` n `787`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
