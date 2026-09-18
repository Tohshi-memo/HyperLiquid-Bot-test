# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T13:37:35.067848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.2353` n `234`; crypto_major avg `0.2878` n `8`; equity avg `0.1414` n `140`; fx avg `0.0049` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0937` n `20`; unknown avg `16.5422` n `928`
- 1h: commodity avg `0.1432` n `12`; crypto_alt avg `0.4158` n `234`; crypto_major avg `0.3138` n `8`; equity avg `0.2503` n `140`; fx avg `0.007` n `6`; index avg `0.0088` n `26`; metal avg `-0.1543` n `20`; unknown avg `9.6674` n `926`
- 4h: commodity avg `0.3392` n `12`; crypto_alt avg `0.4173` n `234`; crypto_major avg `0.5876` n `8`; equity avg `-0.2293` n `140`; fx avg `-0.0525` n `6`; index avg `-0.079` n `26`; metal avg `-0.2338` n `20`; unknown avg `4.4668` n `917`
- 24h: commodity avg `0.3014` n `12`; crypto_alt avg `6.1646` n `234`; crypto_major avg `4.7442` n `8`; equity avg `0.9201` n `140`; fx avg `0.2034` n `6`; index avg `-0.0036` n `26`; metal avg `0.0997` n `20`; unknown avg `2.1152` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
