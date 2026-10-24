# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T18:45:27.775178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `13`; crypto_alt avg `0.091` n `237`; crypto_major avg `0.1023` n `8`; equity avg `0.0438` n `152`; fx avg `-0.0049` n `6`; index avg `0.0047` n `26`; metal avg `-0.0022` n `20`; unknown avg `4.0336` n `1231`
- 1h: commodity avg `0.0021` n `13`; crypto_alt avg `0.4235` n `237`; crypto_major avg `0.2844` n `8`; equity avg `0.0829` n `152`; fx avg `0.0032` n `6`; index avg `0.0103` n `26`; metal avg `0.0002` n `20`; unknown avg `6.6838` n `1231`
- 4h: commodity avg `0.0015` n `13`; crypto_alt avg `0.1864` n `237`; crypto_major avg `0.189` n `8`; equity avg `0.0122` n `152`; fx avg `-0.0123` n `6`; index avg `0.0049` n `26`; metal avg `-0.0163` n `20`; unknown avg `-0.0976` n `1200`
- 24h: commodity avg `0.1675` n `13`; crypto_alt avg `-3.3938` n `237`; crypto_major avg `-2.2058` n `8`; equity avg `-0.7092` n `152`; fx avg `-0.0294` n `6`; index avg `-0.0677` n `26`; metal avg `-0.2084` n `20`; unknown avg `-0.8098` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
