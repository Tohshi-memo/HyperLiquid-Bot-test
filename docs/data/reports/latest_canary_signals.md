# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T20:37:26.665635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `-0.0125` n `239`; crypto_major avg `-0.0449` n `8`; equity avg `0.015` n `158`; fx avg `-0.0166` n `6`; index avg `-0.0021` n `27`; metal avg `0.0017` n `20`; unknown avg `-0.2033` n `1254`
- 1h: commodity avg `-0.009` n `13`; crypto_alt avg `-0.0304` n `239`; crypto_major avg `-0.1719` n `8`; equity avg `-0.056` n `158`; fx avg `-0.0066` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0007` n `20`; unknown avg `-0.1174` n `1240`
- 4h: commodity avg `0.0517` n `13`; crypto_alt avg `-0.074` n `239`; crypto_major avg `-0.0854` n `8`; equity avg `0.1026` n `158`; fx avg `0.001` n `6`; index avg `0.0153` n `27`; metal avg `0.0003` n `20`; unknown avg `-0.0268` n `1209`
- 24h: commodity avg `0.1062` n `13`; crypto_alt avg `-1.4619` n `239`; crypto_major avg `-0.6545` n `8`; equity avg `-0.0046` n `158`; fx avg `-0.0089` n `6`; index avg `0.0347` n `27`; metal avg `-0.0086` n `20`; unknown avg `-0.0397` n `1075`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
