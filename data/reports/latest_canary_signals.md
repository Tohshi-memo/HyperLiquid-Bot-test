# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T22:37:27.656369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `-0.0393` n `239`; crypto_major avg `0.0521` n `8`; equity avg `0.2038` n `168`; fx avg `0.0006` n `6`; index avg `0.0101` n `27`; metal avg `0.0002` n `20`; unknown avg `41.0854` n `1263`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `-0.1237` n `239`; crypto_major avg `-0.4278` n `8`; equity avg `0.0286` n `168`; fx avg `-0.012` n `6`; index avg `-0.0267` n `27`; metal avg `0.1228` n `20`; unknown avg `43.6261` n `1245`
- 4h: commodity avg `0.0174` n `13`; crypto_alt avg `0.937` n `239`; crypto_major avg `1.0049` n `8`; equity avg `1.2665` n `168`; fx avg `-0.0197` n `6`; index avg `0.0801` n `27`; metal avg `0.5009` n `20`; unknown avg `7.3569` n `1197`
- 24h: commodity avg `0.4314` n `13`; crypto_alt avg `1.9282` n `239`; crypto_major avg `0.7565` n `8`; equity avg `-0.9238` n `168`; fx avg `0.0432` n `6`; index avg `-0.0991` n `27`; metal avg `0.2313` n `20`; unknown avg `-0.1579` n `1055`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
