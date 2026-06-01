# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T11:22:22.388333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1311` n `12`; crypto_alt avg `0.1301` n `228`; crypto_major avg `0.1653` n `8`; equity avg `-0.1675` n `69`; fx avg `0.0033` n `6`; index avg `-0.0302` n `23`; metal avg `0.1138` n `18`; unknown avg `0.0357` n `420`
- 1h: commodity avg `-0.2357` n `12`; crypto_alt avg `0.2456` n `228`; crypto_major avg `0.2573` n `8`; equity avg `-0.1849` n `69`; fx avg `-0.0131` n `6`; index avg `-0.0479` n `23`; metal avg `0.0764` n `18`; unknown avg `0.0619` n `420`
- 4h: commodity avg `-0.344` n `12`; crypto_alt avg `-0.0756` n `228`; crypto_major avg `0.1942` n `8`; equity avg `-0.4061` n `69`; fx avg `-0.0157` n `6`; index avg `-0.6323` n `23`; metal avg `0.1804` n `18`; unknown avg `0.375` n `420`
- 24h: commodity avg `0.81` n `12`; crypto_alt avg `-0.191` n `228`; crypto_major avg `-0.2854` n `8`; equity avg `-0.3393` n `69`; fx avg `0.0202` n `6`; index avg `0.4607` n `23`; metal avg `0.3177` n `18`; unknown avg `2.3027` n `409`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2867`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
