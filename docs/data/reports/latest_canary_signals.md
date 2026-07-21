# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T18:52:27.244725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `0.0427` n `230`; crypto_major avg `-0.0642` n `8`; equity avg `-0.083` n `98`; fx avg `0.015` n `6`; index avg `0.0013` n `25`; metal avg `-0.0099` n `20`; unknown avg `0.013` n `771`
- 1h: commodity avg `0.07` n `12`; crypto_alt avg `0.3601` n `230`; crypto_major avg `0.0322` n `8`; equity avg `-0.257` n `98`; fx avg `0.0087` n `6`; index avg `-0.0122` n `25`; metal avg `0.0688` n `20`; unknown avg `0.0166` n `771`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `0.0053` n `230`; crypto_major avg `-0.5467` n `8`; equity avg `0.5202` n `98`; fx avg `0.0221` n `6`; index avg `0.1212` n `25`; metal avg `0.0596` n `20`; unknown avg `0.1087` n `771`
- 24h: commodity avg `0.2757` n `12`; crypto_alt avg `0.8284` n `230`; crypto_major avg `0.6194` n `8`; equity avg `3.2491` n `98`; fx avg `0.0489` n `6`; index avg `0.5755` n `25`; metal avg `0.7272` n `20`; unknown avg `0.1835` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0896`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0599`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0536`, n `666`, weak_sample_signal
