# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T02:07:27.791687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1268` n `12`; crypto_alt avg `-0.0579` n `230`; crypto_major avg `-0.0941` n `8`; equity avg `-0.1944` n `102`; fx avg `-0.0229` n `6`; index avg `-0.029` n `25`; metal avg `0.0205` n `20`; unknown avg `-0.001` n `779`
- 1h: commodity avg `-0.1349` n `12`; crypto_alt avg `-0.408` n `230`; crypto_major avg `-0.4542` n `8`; equity avg `-0.7327` n `102`; fx avg `-0.0097` n `6`; index avg `-0.1865` n `25`; metal avg `-0.0663` n `20`; unknown avg `1.0402` n `779`
- 4h: commodity avg `-0.3612` n `12`; crypto_alt avg `-0.1054` n `230`; crypto_major avg `-0.3914` n `8`; equity avg `0.6786` n `102`; fx avg `0.1988` n `6`; index avg `0.2613` n `25`; metal avg `-0.1971` n `20`; unknown avg `0.268` n `779`
- 24h: commodity avg `-0.2801` n `12`; crypto_alt avg `0.011` n `230`; crypto_major avg `0.6396` n `8`; equity avg `6.5611` n `102`; fx avg `-0.2215` n `6`; index avg `0.7704` n `25`; metal avg `0.258` n `20`; unknown avg `0.0526` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
