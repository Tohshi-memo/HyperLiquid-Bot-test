# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T02:22:32.688807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.0381` n `228`; crypto_major avg `0.0096` n `8`; equity avg `-0.1232` n `86`; fx avg `-0.0103` n `6`; index avg `-0.0164` n `23`; metal avg `0.1815` n `20`; unknown avg `0.2655` n `748`
- 1h: commodity avg `-0.0955` n `12`; crypto_alt avg `0.1388` n `228`; crypto_major avg `0.0999` n `8`; equity avg `-0.0852` n `86`; fx avg `-0.0041` n `6`; index avg `0.0651` n `23`; metal avg `-0.118` n `20`; unknown avg `0.2156` n `748`
- 4h: commodity avg `-0.0863` n `12`; crypto_alt avg `-0.2077` n `228`; crypto_major avg `0.0834` n `8`; equity avg `-0.5273` n `86`; fx avg `0.0942` n `6`; index avg `-0.0485` n `23`; metal avg `-0.2062` n `20`; unknown avg `-0.3702` n `732`
- 24h: commodity avg `-0.5692` n `12`; crypto_alt avg `-2.2138` n `228`; crypto_major avg `-1.8376` n `8`; equity avg `-0.52` n `86`; fx avg `0.0741` n `6`; index avg `0.4506` n `23`; metal avg `-1.5866` n `20`; unknown avg `-0.7517` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
