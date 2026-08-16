# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T08:22:26.979504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0238` n `230`; crypto_major avg `0.0338` n `8`; equity avg `0.0234` n `114`; fx avg `-0.0074` n `6`; index avg `0.0039` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0643` n `791`
- 1h: commodity avg `0.0404` n `12`; crypto_alt avg `0.179` n `230`; crypto_major avg `0.0974` n `8`; equity avg `0.02` n `114`; fx avg `-0.0031` n `6`; index avg `0.0017` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.0563` n `791`
- 4h: commodity avg `-0.0314` n `12`; crypto_alt avg `0.3912` n `230`; crypto_major avg `0.051` n `8`; equity avg `0.1107` n `114`; fx avg `-0.001` n `6`; index avg `0.0251` n `25`; metal avg `0.008` n `20`; unknown avg `-0.0065` n `759`
- 24h: commodity avg `0.1194` n `12`; crypto_alt avg `0.1003` n `230`; crypto_major avg `0.1338` n `8`; equity avg `0.4003` n `114`; fx avg `-0.0206` n `6`; index avg `0.0582` n `25`; metal avg `0.014` n `20`; unknown avg `-0.0191` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
