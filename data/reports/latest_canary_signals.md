# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T18:37:35.663334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0763` n `12`; crypto_alt avg `-0.2621` n `234`; crypto_major avg `-0.1653` n `8`; equity avg `-0.0814` n `140`; fx avg `0.0059` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0192` n `20`; unknown avg `28.2904` n `942`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `0.038` n `234`; crypto_major avg `-0.0737` n `8`; equity avg `0.1888` n `140`; fx avg `0.0197` n `6`; index avg `0.0434` n `26`; metal avg `0.2076` n `20`; unknown avg `27.9273` n `940`
- 4h: commodity avg `0.1038` n `12`; crypto_alt avg `1.8553` n `234`; crypto_major avg `1.0675` n `8`; equity avg `0.0968` n `140`; fx avg `0.0216` n `6`; index avg `0.0099` n `26`; metal avg `0.2108` n `20`; unknown avg `22.7922` n `880`
- 24h: commodity avg `0.1601` n `12`; crypto_alt avg `2.4451` n `234`; crypto_major avg `1.227` n `8`; equity avg `0.7996` n `140`; fx avg `-0.2691` n `6`; index avg `0.1094` n `26`; metal avg `0.2135` n `20`; unknown avg `21.7074` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
