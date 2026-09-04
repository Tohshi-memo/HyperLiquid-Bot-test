# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T05:52:25.257340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `-0.383` n `232`; crypto_major avg `-0.2573` n `8`; equity avg `-0.1225` n `133`; fx avg `-0.0008` n `6`; index avg `-0.024` n `26`; metal avg `-0.0282` n `20`; unknown avg `4.1782` n `793`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.5991` n `232`; crypto_major avg `-0.4273` n `8`; equity avg `-0.0273` n `133`; fx avg `-0.0208` n `6`; index avg `0.0212` n `26`; metal avg `-0.0617` n `20`; unknown avg `1.4949` n `791`
- 4h: commodity avg `-0.0859` n `12`; crypto_alt avg `-0.6913` n `232`; crypto_major avg `-0.2408` n `8`; equity avg `0.3011` n `133`; fx avg `-0.0318` n `6`; index avg `0.0944` n `26`; metal avg `-0.0684` n `20`; unknown avg `10.0327` n `791`
- 24h: commodity avg `0.0215` n `12`; crypto_alt avg `1.7495` n `232`; crypto_major avg `3.7711` n `8`; equity avg `1.8646` n `133`; fx avg `-0.1182` n `6`; index avg `0.3341` n `26`; metal avg `0.4208` n `20`; unknown avg `1.7334` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
