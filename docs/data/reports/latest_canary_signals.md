# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T01:07:23.217534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0294` n `13`; crypto_alt avg `0.0147` n `239`; crypto_major avg `0.0867` n `8`; equity avg `-0.0609` n `168`; fx avg `0.0168` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0114` n `20`; unknown avg `0.761` n `1251`
- 1h: commodity avg `-0.1216` n `13`; crypto_alt avg `-0.1957` n `239`; crypto_major avg `0.0833` n `8`; equity avg `-0.1528` n `168`; fx avg `0.0217` n `6`; index avg `-0.0153` n `27`; metal avg `-0.0283` n `20`; unknown avg `128.5145` n `1257`
- 4h: commodity avg `-0.1083` n `13`; crypto_alt avg `0.0744` n `239`; crypto_major avg `-0.0206` n `8`; equity avg `-0.124` n `168`; fx avg `0.0046` n `6`; index avg `0.0069` n `27`; metal avg `-0.0093` n `20`; unknown avg `1.3149` n `1165`
- 24h: commodity avg `-0.6876` n `13`; crypto_alt avg `0.0586` n `239`; crypto_major avg `0.0847` n `8`; equity avg `3.0269` n `168`; fx avg `-0.1215` n `6`; index avg `0.3005` n `27`; metal avg `0.8955` n `20`; unknown avg `213.8633` n `985`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
