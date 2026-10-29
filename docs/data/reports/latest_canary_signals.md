# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T07:52:47.685142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `-0.1062` n `238`; crypto_major avg `-0.056` n `8`; equity avg `-0.0555` n `155`; fx avg `0.0006` n `6`; index avg `-0.0256` n `27`; metal avg `-0.0399` n `20`; unknown avg `0.0582` n `1238`
- 1h: commodity avg `0.0684` n `13`; crypto_alt avg `-0.4741` n `238`; crypto_major avg `-0.309` n `8`; equity avg `-0.3139` n `155`; fx avg `0.0348` n `6`; index avg `-0.0753` n `27`; metal avg `-0.087` n `20`; unknown avg `8.0077` n `1230`
- 4h: commodity avg `0.0706` n `13`; crypto_alt avg `-0.3665` n `238`; crypto_major avg `0.0962` n `8`; equity avg `-0.0286` n `155`; fx avg `0.0278` n `6`; index avg `0.0682` n `27`; metal avg `-0.1588` n `20`; unknown avg `0.1983` n `1192`
- 24h: commodity avg `-0.1965` n `13`; crypto_alt avg `-2.8615` n `238`; crypto_major avg `-1.8096` n `8`; equity avg `-1.5176` n `154`; fx avg `0.0653` n `6`; index avg `-0.0849` n `27`; metal avg `-0.3589` n `20`; unknown avg `30.3677` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
