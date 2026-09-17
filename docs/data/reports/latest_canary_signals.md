# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T19:07:09.631316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0747` n `12`; crypto_alt avg `-0.0213` n `234`; crypto_major avg `-0.0382` n `8`; equity avg `0.0709` n `140`; fx avg `-0.0001` n `6`; index avg `0.0201` n `26`; metal avg `0.0088` n `20`; unknown avg `2.9908` n `915`
- 1h: commodity avg `-0.0857` n `12`; crypto_alt avg `-0.1695` n `234`; crypto_major avg `-0.2323` n `8`; equity avg `0.0425` n `140`; fx avg `-0.0015` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0802` n `20`; unknown avg `1.2607` n `915`
- 4h: commodity avg `0.0256` n `12`; crypto_alt avg `0.9854` n `234`; crypto_major avg `0.2175` n `8`; equity avg `0.3631` n `140`; fx avg `0.0056` n `6`; index avg `0.0617` n `26`; metal avg `-0.0615` n `20`; unknown avg `2.4325` n `907`
- 24h: commodity avg `-0.1679` n `12`; crypto_alt avg `3.9866` n `234`; crypto_major avg `1.4951` n `8`; equity avg `2.8957` n `138`; fx avg `0.0464` n `6`; index avg `0.5361` n `26`; metal avg `0.6563` n `20`; unknown avg `1.6593` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
