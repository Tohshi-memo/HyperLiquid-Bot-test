# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T14:22:28.297644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.0135` n `230`; crypto_major avg `-0.064` n `8`; equity avg `-0.0162` n `114`; fx avg `-0.0068` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0141` n `791`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `0.0482` n `230`; crypto_major avg `-0.0843` n `8`; equity avg `0.0103` n `114`; fx avg `-0.0043` n `6`; index avg `-0.0023` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0004` n `791`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.043` n `230`; crypto_major avg `0.0169` n `8`; equity avg `0.034` n `114`; fx avg `-0.0052` n `6`; index avg `0.0195` n `25`; metal avg `-0.0054` n `20`; unknown avg `-0.1861` n `791`
- 24h: commodity avg `-0.0579` n `12`; crypto_alt avg `1.1874` n `230`; crypto_major avg `0.5759` n `8`; equity avg `-0.2291` n `114`; fx avg `0.0672` n `6`; index avg `-0.0658` n `25`; metal avg `-0.021` n `20`; unknown avg `0.0306` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
