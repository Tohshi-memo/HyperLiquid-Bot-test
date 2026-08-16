# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T19:07:23.841225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0058` n `230`; crypto_major avg `0.0187` n `8`; equity avg `0.0162` n `114`; fx avg `0.0012` n `6`; index avg `0.0013` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.1075` n `791`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.0246` n `230`; crypto_major avg `0.0444` n `8`; equity avg `0.0128` n `114`; fx avg `0.0025` n `6`; index avg `0.0098` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.1286` n `791`
- 4h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.1292` n `230`; crypto_major avg `0.0438` n `8`; equity avg `0.0912` n `114`; fx avg `0.0136` n `6`; index avg `0.0046` n `25`; metal avg `0.0304` n `20`; unknown avg `-0.1291` n `791`
- 24h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.3088` n `230`; crypto_major avg `0.0353` n `8`; equity avg `0.31` n `114`; fx avg `-0.0024` n `6`; index avg `0.0269` n `25`; metal avg `0.0568` n `20`; unknown avg `0.1043` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
