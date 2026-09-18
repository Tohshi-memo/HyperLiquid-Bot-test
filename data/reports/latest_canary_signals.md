# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T20:18:14.165262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.1854` n `234`; crypto_major avg `0.1718` n `8`; equity avg `0.0273` n `140`; fx avg `0.0027` n `6`; index avg `0.0123` n `26`; metal avg `0.0081` n `20`; unknown avg `15.1155` n `934`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `0.1901` n `234`; crypto_major avg `0.271` n `8`; equity avg `0.341` n `140`; fx avg `0.0101` n `6`; index avg `0.0838` n `26`; metal avg `-0.0076` n `20`; unknown avg `2809.3559` n `910`
- 4h: commodity avg `-0.2259` n `12`; crypto_alt avg `0.9439` n `234`; crypto_major avg `1.0002` n `8`; equity avg `0.9252` n `140`; fx avg `0.0091` n `6`; index avg `0.1955` n `26`; metal avg `0.0307` n `20`; unknown avg `17.2118` n `892`
- 24h: commodity avg `-0.0923` n `12`; crypto_alt avg `6.6647` n `234`; crypto_major avg `7.1217` n `8`; equity avg `1.3556` n `140`; fx avg `0.2093` n `6`; index avg `0.0656` n `26`; metal avg `0.4005` n `20`; unknown avg `9.548` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
