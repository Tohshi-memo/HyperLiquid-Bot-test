# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T19:52:30.407379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.1233` n `234`; crypto_major avg `0.2178` n `8`; equity avg `0.1613` n `140`; fx avg `0.0032` n `6`; index avg `0.0371` n `26`; metal avg `-0.0134` n `20`; unknown avg `10.173` n `940`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `0.6226` n `234`; crypto_major avg `0.7925` n `8`; equity avg `0.3365` n `140`; fx avg `0.0064` n `6`; index avg `0.0561` n `26`; metal avg `-0.0261` n `20`; unknown avg `25.8291` n `936`
- 4h: commodity avg `-0.2838` n `12`; crypto_alt avg `1.0651` n `234`; crypto_major avg `1.3617` n `8`; equity avg `0.6349` n `140`; fx avg `0.0041` n `6`; index avg `0.1372` n `26`; metal avg `0.0842` n `20`; unknown avg `16.5062` n `906`
- 24h: commodity avg `-0.0578` n `12`; crypto_alt avg `6.8118` n `234`; crypto_major avg `7.3124` n `8`; equity avg `1.1763` n `140`; fx avg `0.2029` n `6`; index avg `-0.0132` n `26`; metal avg `0.3601` n `20`; unknown avg `10.738` n `715`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
