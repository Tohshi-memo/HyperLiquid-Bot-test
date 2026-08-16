# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T20:34:03.001036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0377` n `12`; crypto_alt avg `0.012` n `230`; crypto_major avg `-0.0333` n `8`; equity avg `-0.0105` n `114`; fx avg `0.0001` n `6`; index avg `0.0006` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0479` n `791`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0243` n `230`; crypto_major avg `-0.1405` n `8`; equity avg `-0.0097` n `114`; fx avg `0.0056` n `6`; index avg `-0.005` n `25`; metal avg `-0.0266` n `20`; unknown avg `0.104` n `791`
- 4h: commodity avg `0.0855` n `12`; crypto_alt avg `-0.2388` n `230`; crypto_major avg `-0.2572` n `8`; equity avg `0.0167` n `114`; fx avg `-0.0012` n `6`; index avg `0.0038` n `25`; metal avg `-0.0129` n `20`; unknown avg `0.0741` n `791`
- 24h: commodity avg `0.0579` n `12`; crypto_alt avg `-0.1522` n `230`; crypto_major avg `-0.0054` n `8`; equity avg `0.2614` n `114`; fx avg `-0.0051` n `6`; index avg `0.0452` n `25`; metal avg `0.0274` n `20`; unknown avg `0.0808` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2182`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
