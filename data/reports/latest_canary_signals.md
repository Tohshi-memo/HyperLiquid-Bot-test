# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T08:52:29.785260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `0.1433` n `234`; crypto_major avg `0.0723` n `8`; equity avg `0.0054` n `140`; fx avg `0.0013` n `6`; index avg `0.0009` n `26`; metal avg `0.0256` n `20`; unknown avg `0.7278` n `927`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `0.1836` n `234`; crypto_major avg `0.0734` n `8`; equity avg `0.0465` n `140`; fx avg `0.0411` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0304` n `20`; unknown avg `0.5054` n `919`
- 4h: commodity avg `-0.1172` n `12`; crypto_alt avg `0.7237` n `234`; crypto_major avg `0.6608` n `8`; equity avg `0.4628` n `140`; fx avg `0.0512` n `6`; index avg `0.0655` n `26`; metal avg `0.281` n `20`; unknown avg `-0.0125` n `863`
- 24h: commodity avg `-0.2243` n `12`; crypto_alt avg `5.1354` n `234`; crypto_major avg `3.7899` n `8`; equity avg `1.9755` n `140`; fx avg `0.1912` n `6`; index avg `0.3208` n `26`; metal avg `0.8007` n `20`; unknown avg `2.4631` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
