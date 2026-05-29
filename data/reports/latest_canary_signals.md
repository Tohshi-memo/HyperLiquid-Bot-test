# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T04:07:19.565913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0644` n `12`; crypto_alt avg `-0.0925` n `228`; crypto_major avg `-0.0621` n `8`; equity avg `0.0665` n `69`; fx avg `-0.0076` n `6`; index avg `0.0439` n `23`; metal avg `0.0758` n `18`; unknown avg `-0.0786` n `417`
- 1h: commodity avg `0.1611` n `12`; crypto_alt avg `-0.4525` n `228`; crypto_major avg `-0.2212` n `8`; equity avg `0.1583` n `69`; fx avg `-0.0005` n `6`; index avg `0.0616` n `23`; metal avg `-0.0372` n `18`; unknown avg `-0.317` n `417`
- 4h: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.6999` n `228`; crypto_major avg `-0.4813` n `8`; equity avg `0.0516` n `69`; fx avg `0.0183` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0747` n `18`; unknown avg `-0.6513` n `417`
- 24h: commodity avg `-0.2057` n `12`; crypto_alt avg `0.265` n `228`; crypto_major avg `1.5791` n `8`; equity avg `4.6002` n `69`; fx avg `0.1402` n `6`; index avg `1.5524` n `23`; metal avg `2.2005` n `18`; unknown avg `0.4643` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
