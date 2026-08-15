# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T06:52:26.683104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.0155` n `230`; crypto_major avg `0.0715` n `8`; equity avg `0.0402` n `114`; fx avg `0.0049` n `6`; index avg `0.0055` n `25`; metal avg `0.0098` n `20`; unknown avg `0.0061` n `791`
- 1h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.0236` n `230`; crypto_major avg `0.0986` n `8`; equity avg `0.0206` n `114`; fx avg `0.0037` n `6`; index avg `0.0064` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.044` n `765`
- 4h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.2185` n `230`; crypto_major avg `-0.0397` n `8`; equity avg `-0.0111` n `114`; fx avg `-0.0361` n `6`; index avg `-0.0227` n `25`; metal avg `-0.0284` n `20`; unknown avg `-0.0172` n `759`
- 24h: commodity avg `-0.037` n `12`; crypto_alt avg `0.9253` n `230`; crypto_major avg `0.1496` n `8`; equity avg `-0.1061` n `114`; fx avg `0.1133` n `6`; index avg `-0.0689` n `25`; metal avg `0.3122` n `20`; unknown avg `-0.1623` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
