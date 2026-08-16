# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T09:07:28.792629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `0.014` n `8`; equity avg `0.0096` n `114`; fx avg `-0.0016` n `6`; index avg `0.0029` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0062` n `791`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `0.0448` n `230`; crypto_major avg `0.0637` n `8`; equity avg `0.0467` n `114`; fx avg `-0.0077` n `6`; index avg `0.0049` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0666` n `791`
- 4h: commodity avg `0.0166` n `12`; crypto_alt avg `0.3486` n `230`; crypto_major avg `0.1194` n `8`; equity avg `0.1559` n `114`; fx avg `0.0024` n `6`; index avg `0.0222` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0579` n `759`
- 24h: commodity avg `0.1263` n `12`; crypto_alt avg `0.1187` n `230`; crypto_major avg `0.3683` n `8`; equity avg `0.4521` n `114`; fx avg `-0.0095` n `6`; index avg `0.0559` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0539` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
