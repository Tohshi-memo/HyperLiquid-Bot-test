# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T01:52:30.704287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `13`; crypto_alt avg `0.0208` n `239`; crypto_major avg `0.1817` n `8`; equity avg `-0.1611` n `168`; fx avg `-0.0087` n `6`; index avg `-0.0236` n `27`; metal avg `-0.0162` n `20`; unknown avg `-0.2815` n `1267`
- 1h: commodity avg `-0.0071` n `13`; crypto_alt avg `0.2231` n `239`; crypto_major avg `0.4001` n `8`; equity avg `-0.3028` n `168`; fx avg `-0.03` n `6`; index avg `-0.0386` n `27`; metal avg `-0.0548` n `20`; unknown avg `19.1251` n `1259`
- 4h: commodity avg `-0.03` n `13`; crypto_alt avg `0.9737` n `239`; crypto_major avg `0.525` n `8`; equity avg `1.2901` n `168`; fx avg `-0.0431` n `6`; index avg `0.1025` n `27`; metal avg `-0.0725` n `20`; unknown avg `44.3228` n `1185`
- 24h: commodity avg `0.469` n `13`; crypto_alt avg `4.1784` n `239`; crypto_major avg `3.1202` n `8`; equity avg `1.5383` n `168`; fx avg `-0.0094` n `6`; index avg `0.147` n `27`; metal avg `0.0758` n `20`; unknown avg `770.5321` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
