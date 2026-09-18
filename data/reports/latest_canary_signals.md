# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T06:22:35.675886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0445` n `12`; crypto_alt avg `0.1074` n `234`; crypto_major avg `0.084` n `8`; equity avg `0.0781` n `140`; fx avg `-0.0023` n `6`; index avg `0.0122` n `26`; metal avg `-0.0021` n `20`; unknown avg `1.0302` n `919`
- 1h: commodity avg `-0.0799` n `12`; crypto_alt avg `0.0837` n `234`; crypto_major avg `0.1732` n `8`; equity avg `0.1991` n `140`; fx avg `-0.0606` n `6`; index avg `0.0079` n `26`; metal avg `0.1218` n `20`; unknown avg `7.4939` n `881`
- 4h: commodity avg `-0.1129` n `12`; crypto_alt avg `1.3768` n `234`; crypto_major avg `1.4639` n `8`; equity avg `0.9442` n `140`; fx avg `0.0634` n `6`; index avg `0.1395` n `26`; metal avg `0.302` n `20`; unknown avg `4.9891` n `863`
- 24h: commodity avg `-0.2026` n `12`; crypto_alt avg `5.1341` n `234`; crypto_major avg `3.9801` n `8`; equity avg `2.5177` n `140`; fx avg `0.1325` n `6`; index avg `0.3694` n `26`; metal avg `0.6514` n `20`; unknown avg `4.5535` n `741`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
