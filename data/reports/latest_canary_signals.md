# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T19:37:32.774078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.0543` n `234`; crypto_major avg `-0.1259` n `8`; equity avg `-0.0989` n `141`; fx avg `-0.0109` n `6`; index avg `-0.0016` n `26`; metal avg `0.0` n `20`; unknown avg `324.6967` n `938`
- 1h: commodity avg `0.1763` n `12`; crypto_alt avg `0.6255` n `234`; crypto_major avg `0.1646` n `8`; equity avg `0.0066` n `141`; fx avg `0.0009` n `6`; index avg `0.0056` n `26`; metal avg `0.0085` n `20`; unknown avg `56.0118` n `935`
- 4h: commodity avg `-0.0508` n `12`; crypto_alt avg `0.6496` n `234`; crypto_major avg `0.4183` n `8`; equity avg `0.7793` n `141`; fx avg `-0.0191` n `6`; index avg `0.1233` n `26`; metal avg `0.197` n `20`; unknown avg `7.9466` n `923`
- 24h: commodity avg `0.9976` n `12`; crypto_alt avg `3.901` n `234`; crypto_major avg `1.4409` n `8`; equity avg `-0.4334` n `141`; fx avg `0.0426` n `6`; index avg `-0.0994` n `26`; metal avg `-0.0418` n `20`; unknown avg `266.0327` n `831`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
