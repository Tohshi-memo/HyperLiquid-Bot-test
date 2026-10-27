# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T08:37:28.845614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `13`; crypto_alt avg `-0.229` n `238`; crypto_major avg `-0.1295` n `8`; equity avg `-0.1578` n `154`; fx avg `-0.0195` n `6`; index avg `-0.0315` n `27`; metal avg `-0.0213` n `20`; unknown avg `192.3819` n `1236`
- 1h: commodity avg `0.0906` n `13`; crypto_alt avg `-0.1918` n `238`; crypto_major avg `0.0676` n `8`; equity avg `0.2061` n `154`; fx avg `0.0048` n `6`; index avg `0.007` n `27`; metal avg `0.0038` n `20`; unknown avg `-0.1321` n `1202`
- 4h: commodity avg `0.3625` n `13`; crypto_alt avg `0.221` n `237`; crypto_major avg `0.058` n `8`; equity avg `-0.4263` n `154`; fx avg `-0.0107` n `6`; index avg `-0.0112` n `27`; metal avg `-0.2869` n `20`; unknown avg `-0.192` n `1170`
- 24h: commodity avg `0.2977` n `13`; crypto_alt avg `-0.2234` n `237`; crypto_major avg `-0.0347` n `8`; equity avg `0.6641` n `153`; fx avg `-0.0385` n `6`; index avg `0.2733` n `27`; metal avg `-0.3928` n `20`; unknown avg `1013.3664` n `1040`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
