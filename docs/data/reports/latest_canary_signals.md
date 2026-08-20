# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T05:22:14.438820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.0866` n `230`; crypto_major avg `0.0111` n `8`; equity avg `0.0378` n `121`; fx avg `-0.0044` n `6`; index avg `0.0197` n `25`; metal avg `-0.0665` n `20`; unknown avg `-0.0559` n `792`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.271` n `230`; crypto_major avg `0.4327` n `8`; equity avg `-0.139` n `121`; fx avg `-0.0018` n `6`; index avg `-0.0347` n `25`; metal avg `-0.0724` n `20`; unknown avg `0.1519` n `792`
- 4h: commodity avg `-0.012` n `12`; crypto_alt avg `0.2256` n `230`; crypto_major avg `0.3337` n `8`; equity avg `-0.0004` n `121`; fx avg `0.0327` n `6`; index avg `0.0302` n `25`; metal avg `-0.0355` n `20`; unknown avg `0.0847` n `792`
- 24h: commodity avg `-0.061` n `12`; crypto_alt avg `5.6218` n `230`; crypto_major avg `9.9718` n `8`; equity avg `1.4908` n `120`; fx avg `0.0866` n `6`; index avg `0.3552` n `25`; metal avg `1.1059` n `20`; unknown avg `1.705` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
