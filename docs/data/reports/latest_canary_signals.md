# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T12:37:27.994635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0808` n `12`; crypto_alt avg `0.4324` n `230`; crypto_major avg `0.3889` n `8`; equity avg `0.1131` n `121`; fx avg `-0.0061` n `6`; index avg `0.0194` n `25`; metal avg `-0.074` n `20`; unknown avg `-0.0107` n `793`
- 1h: commodity avg `0.0825` n `12`; crypto_alt avg `0.891` n `230`; crypto_major avg `0.1342` n `8`; equity avg `-0.0692` n `121`; fx avg `0.0241` n `6`; index avg `-0.0107` n `25`; metal avg `-0.1721` n `20`; unknown avg `-0.032` n `793`
- 4h: commodity avg `0.093` n `12`; crypto_alt avg `1.4059` n `230`; crypto_major avg `-0.5356` n `8`; equity avg `0.1833` n `121`; fx avg `0.0559` n `6`; index avg `0.0364` n `25`; metal avg `-0.1905` n `20`; unknown avg `0.3576` n `793`
- 24h: commodity avg `-0.0043` n `12`; crypto_alt avg `8.122` n `230`; crypto_major avg `6.2822` n `8`; equity avg `2.025` n `121`; fx avg `-0.086` n `6`; index avg `0.3137` n `25`; metal avg `0.974` n `20`; unknown avg `2.4047` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
