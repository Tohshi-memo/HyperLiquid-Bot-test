# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T20:52:28.178283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `0.2449` n `231`; crypto_major avg `0.1471` n `8`; equity avg `0.2288` n `122`; fx avg `0.003` n `6`; index avg `0.0426` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.0607` n `797`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.1561` n `231`; crypto_major avg `-0.1939` n `8`; equity avg `0.6092` n `122`; fx avg `-0.0056` n `6`; index avg `0.0448` n `25`; metal avg `-0.0255` n `20`; unknown avg `-0.048` n `797`
- 4h: commodity avg `-0.2258` n `12`; crypto_alt avg `0.6907` n `231`; crypto_major avg `0.6237` n `8`; equity avg `1.0383` n `122`; fx avg `-0.0152` n `6`; index avg `0.1106` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.2039` n `797`
- 24h: commodity avg `0.3131` n `12`; crypto_alt avg `-0.191` n `231`; crypto_major avg `-0.3733` n `8`; equity avg `0.4646` n `122`; fx avg `-0.0485` n `6`; index avg `0.0526` n `25`; metal avg `-0.4197` n `20`; unknown avg `0.6881` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
