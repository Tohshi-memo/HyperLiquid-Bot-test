# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T06:37:26.080489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.1592` n `230`; crypto_major avg `0.0871` n `8`; equity avg `0.1067` n `98`; fx avg `-0.0293` n `6`; index avg `0.0194` n `25`; metal avg `-0.1188` n `20`; unknown avg `0.0389` n `772`
- 1h: commodity avg `0.136` n `12`; crypto_alt avg `-0.167` n `230`; crypto_major avg `-0.2859` n `8`; equity avg `-0.2051` n `98`; fx avg `-0.0478` n `6`; index avg `-0.0847` n `25`; metal avg `-0.151` n `20`; unknown avg `-0.0728` n `739`
- 4h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.8312` n `230`; crypto_major avg `-1.116` n `8`; equity avg `-1.2967` n `98`; fx avg `-0.0356` n `6`; index avg `-0.2819` n `25`; metal avg `-0.1747` n `20`; unknown avg `-0.2174` n `739`
- 24h: commodity avg `0.7042` n `12`; crypto_alt avg `-1.1382` n `230`; crypto_major avg `-1.6563` n `8`; equity avg `0.8741` n `98`; fx avg `0.0094` n `6`; index avg `0.0215` n `25`; metal avg `0.3341` n `20`; unknown avg `0.0608` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0976`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0782`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.07`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
