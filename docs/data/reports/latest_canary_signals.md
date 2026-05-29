# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T13:22:19.824693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2114` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2522` n `12`; crypto_alt avg `-0.0596` n `228`; crypto_major avg `-0.0676` n `8`; equity avg `-0.1196` n `69`; fx avg `0.0308` n `6`; index avg `0.0349` n `23`; metal avg `0.1565` n `18`; unknown avg `0.936` n `417`
- 1h: commodity avg `0.1638` n `12`; crypto_alt avg `-0.6918` n `228`; crypto_major avg `-0.2975` n `8`; equity avg `-0.085` n `69`; fx avg `0.0494` n `6`; index avg `0.0542` n `23`; metal avg `0.4543` n `18`; unknown avg `1.093` n `417`
- 4h: commodity avg `0.321` n `12`; crypto_alt avg `-1.6588` n `228`; crypto_major avg `-1.1053` n `8`; equity avg `-0.3894` n `69`; fx avg `0.0585` n `6`; index avg `0.1061` n `23`; metal avg `0.2513` n `18`; unknown avg `-0.0678` n `417`
- 24h: commodity avg `0.2177` n `12`; crypto_alt avg `0.6336` n `228`; crypto_major avg `1.5835` n `8`; equity avg `2.8915` n `69`; fx avg `0.1073` n `6`; index avg `1.3267` n `23`; metal avg `1.7713` n `18`; unknown avg `1.965` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
