# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T06:22:30.374995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0725` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1279` n `12`; crypto_alt avg `-0.1578` n `230`; crypto_major avg `-0.1504` n `8`; equity avg `-0.1065` n `98`; fx avg `-0.0043` n `6`; index avg `-0.0567` n `25`; metal avg `-0.0329` n `20`; unknown avg `0.0013` n `772`
- 1h: commodity avg `0.1077` n `12`; crypto_alt avg `-0.379` n `230`; crypto_major avg `-0.492` n `8`; equity avg `-0.4747` n `98`; fx avg `-0.0127` n `6`; index avg `-0.1205` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.0867` n `739`
- 4h: commodity avg `0.0845` n `12`; crypto_alt avg `-1.1086` n `230`; crypto_major avg `-1.397` n `8`; equity avg `-1.5459` n `98`; fx avg `-0.0087` n `6`; index avg `-0.3245` n `25`; metal avg `-0.058` n `20`; unknown avg `-0.2231` n `739`
- 24h: commodity avg `0.6827` n `12`; crypto_alt avg `-1.1409` n `230`; crypto_major avg `-1.4731` n `8`; equity avg `0.7934` n `98`; fx avg `0.0432` n `6`; index avg `0.0228` n `25`; metal avg `0.4891` n `20`; unknown avg `0.0864` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0966`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0751`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
