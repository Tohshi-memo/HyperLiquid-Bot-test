# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T20:07:30.377864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `-0.0782` n `230`; crypto_major avg `-0.073` n `8`; equity avg `-0.1085` n `114`; fx avg `0.0044` n `6`; index avg `0.0006` n `25`; metal avg `0.0059` n `20`; unknown avg `0.033` n `792`
- 1h: commodity avg `0.0575` n `12`; crypto_alt avg `-0.1308` n `230`; crypto_major avg `-0.0866` n `8`; equity avg `-0.1104` n `114`; fx avg `-0.009` n `6`; index avg `-0.0059` n `25`; metal avg `0.0537` n `20`; unknown avg `0.1288` n `792`
- 4h: commodity avg `0.399` n `12`; crypto_alt avg `-0.2773` n `230`; crypto_major avg `-0.2245` n `8`; equity avg `-0.6285` n `114`; fx avg `0.0084` n `6`; index avg `-0.1408` n `25`; metal avg `-0.1118` n `20`; unknown avg `0.1329` n `792`
- 24h: commodity avg `0.3692` n `12`; crypto_alt avg `-0.2566` n `230`; crypto_major avg `0.6868` n `8`; equity avg `0.9774` n `114`; fx avg `0.0131` n `6`; index avg `0.0586` n `25`; metal avg `0.1943` n `20`; unknown avg `0.2463` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
