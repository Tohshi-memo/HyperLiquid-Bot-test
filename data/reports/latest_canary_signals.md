# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T18:37:36.653406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.4716` n `228`; crypto_major avg `-0.3245` n `8`; equity avg `-0.1202` n `86`; fx avg `-0.0015` n `6`; index avg `-0.0237` n `23`; metal avg `-0.0611` n `20`; unknown avg `0.0234` n `765`
- 1h: commodity avg `0.0632` n `12`; crypto_alt avg `-0.6654` n `228`; crypto_major avg `-0.6511` n `8`; equity avg `-0.0245` n `86`; fx avg `0.0108` n `6`; index avg `0.0077` n `23`; metal avg `-0.0367` n `20`; unknown avg `-0.1321` n `765`
- 4h: commodity avg `0.3281` n `12`; crypto_alt avg `-0.2657` n `228`; crypto_major avg `0.4237` n `8`; equity avg `-0.0738` n `86`; fx avg `0.0626` n `6`; index avg `0.017` n `23`; metal avg `0.1648` n `20`; unknown avg `0.413` n `765`
- 24h: commodity avg `0.4461` n `12`; crypto_alt avg `-0.1503` n `228`; crypto_major avg `0.0116` n `8`; equity avg `0.062` n `86`; fx avg `0.07` n `6`; index avg `0.4532` n `23`; metal avg `0.7062` n `20`; unknown avg `0.6703` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
