# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T12:07:26.484419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0726` n `13`; crypto_alt avg `-0.1775` n `239`; crypto_major avg `-0.2381` n `8`; equity avg `-0.4979` n `168`; fx avg `0.0127` n `6`; index avg `-0.0465` n `27`; metal avg `-0.095` n `20`; unknown avg `159.9457` n `1249`
- 1h: commodity avg `0.0452` n `13`; crypto_alt avg `-0.6443` n `239`; crypto_major avg `-0.4622` n `8`; equity avg `-0.7961` n `168`; fx avg `0.0042` n `6`; index avg `-0.1` n `27`; metal avg `-0.2374` n `20`; unknown avg `163.8683` n `1219`
- 4h: commodity avg `0.4189` n `13`; crypto_alt avg `-1.1032` n `239`; crypto_major avg `-0.521` n `8`; equity avg `-1.2749` n `168`; fx avg `0.0257` n `6`; index avg `-0.1932` n `27`; metal avg `-0.1958` n `20`; unknown avg `171.5762` n `1183`
- 24h: commodity avg `0.2703` n `13`; crypto_alt avg `-2.532` n `239`; crypto_major avg `-3.4516` n `8`; equity avg `-5.3028` n `167`; fx avg `-0.0062` n `6`; index avg `-0.4929` n `27`; metal avg `-1.1723` n `20`; unknown avg `428.0578` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
