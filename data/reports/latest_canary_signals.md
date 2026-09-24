# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T18:07:32.440403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1918` n `12`; crypto_alt avg `-0.328` n `234`; crypto_major avg `-0.1397` n `8`; equity avg `-0.2147` n `141`; fx avg `0.011` n `6`; index avg `-0.0141` n `26`; metal avg `0.0219` n `20`; unknown avg `6.6118` n `941`
- 1h: commodity avg `0.1514` n `12`; crypto_alt avg `-0.5702` n `234`; crypto_major avg `-0.3602` n `8`; equity avg `-0.5924` n `141`; fx avg `0.0075` n `6`; index avg `-0.1148` n `26`; metal avg `-0.0816` n `20`; unknown avg `13.313` n `941`
- 4h: commodity avg `0.6698` n `12`; crypto_alt avg `0.8518` n `234`; crypto_major avg `0.4289` n `8`; equity avg `0.2489` n `141`; fx avg `0.0123` n `6`; index avg `-0.0018` n `26`; metal avg `-0.014` n `20`; unknown avg `58.4667` n `883`
- 24h: commodity avg `1.104` n `12`; crypto_alt avg `2.6713` n `234`; crypto_major avg `1.032` n `8`; equity avg `-0.7523` n `141`; fx avg `0.0335` n `6`; index avg `-0.1431` n `26`; metal avg `-0.1667` n `20`; unknown avg `272.2127` n `833`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
