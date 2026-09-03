# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T19:52:34.217401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `-0.0867` n `232`; crypto_major avg `0.0203` n `8`; equity avg `-0.0494` n `133`; fx avg `-0.0048` n `6`; index avg `0.007` n `26`; metal avg `0.0104` n `20`; unknown avg `11.5653` n `792`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.1572` n `232`; crypto_major avg `0.3443` n `8`; equity avg `-0.0952` n `133`; fx avg `-0.001` n `6`; index avg `-0.0182` n `26`; metal avg `0.0054` n `20`; unknown avg `12.0428` n `790`
- 4h: commodity avg `0.0569` n `12`; crypto_alt avg `0.39` n `232`; crypto_major avg `0.4833` n `8`; equity avg `0.1375` n `133`; fx avg `0.0379` n `6`; index avg `0.0285` n `26`; metal avg `-0.019` n `20`; unknown avg `29.2334` n `790`
- 24h: commodity avg `-0.1365` n `12`; crypto_alt avg `4.7503` n `232`; crypto_major avg `5.907` n `8`; equity avg `1.4001` n `133`; fx avg `-0.2576` n `6`; index avg `0.1829` n `26`; metal avg `0.7908` n `20`; unknown avg `31.8481` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
