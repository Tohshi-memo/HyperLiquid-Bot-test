# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T01:07:31.173571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.085` n `12`; crypto_alt avg `0.0548` n `230`; crypto_major avg `-0.0719` n `8`; equity avg `-0.1155` n `108`; fx avg `0.0001` n `6`; index avg `-0.0323` n `25`; metal avg `0.1296` n `20`; unknown avg `1.1163` n `782`
- 1h: commodity avg `0.0527` n `12`; crypto_alt avg `0.1302` n `230`; crypto_major avg `-0.0734` n `8`; equity avg `-0.5982` n `108`; fx avg `-0.0739` n `6`; index avg `-0.1693` n `25`; metal avg `0.2283` n `20`; unknown avg `0.4479` n `782`
- 4h: commodity avg `-0.0467` n `12`; crypto_alt avg `0.1386` n `230`; crypto_major avg `-0.27` n `8`; equity avg `-0.6337` n `108`; fx avg `-0.0581` n `6`; index avg `-0.1823` n `25`; metal avg `0.3517` n `20`; unknown avg `0.097` n `782`
- 24h: commodity avg `-0.1798` n `12`; crypto_alt avg `0.9595` n `230`; crypto_major avg `0.8318` n `8`; equity avg `-1.6321` n `108`; fx avg `-0.0354` n `6`; index avg `-0.3324` n `25`; metal avg `1.1967` n `20`; unknown avg `1.0897` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
