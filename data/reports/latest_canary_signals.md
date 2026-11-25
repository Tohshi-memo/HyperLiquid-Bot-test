# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T19:52:29.007952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1755` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1105` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7103` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `-0.3272` n `239`; crypto_major avg `-0.3415` n `8`; equity avg `-0.2754` n `168`; fx avg `-0.0046` n `6`; index avg `-0.0251` n `27`; metal avg `-0.043` n `20`; unknown avg `157.9575` n `1267`
- 1h: commodity avg `-0.136` n `13`; crypto_alt avg `0.7183` n `239`; crypto_major avg `0.6021` n `8`; equity avg `0.2872` n `168`; fx avg `-0.0035` n `6`; index avg `-0.0142` n `27`; metal avg `0.0507` n `20`; unknown avg `0.7887` n `1263`
- 4h: commodity avg `-0.0131` n `13`; crypto_alt avg `3.3262` n `239`; crypto_major avg `3.1624` n `8`; equity avg `4.8727` n `168`; fx avg `0.0867` n `6`; index avg `0.4919` n `27`; metal avg `1.0519` n `20`; unknown avg `18.2191` n `1254`
- 24h: commodity avg `0.2894` n `13`; crypto_alt avg `1.9658` n `239`; crypto_major avg `1.1078` n `8`; equity avg `-0.6611` n `168`; fx avg `0.0458` n `6`; index avg `-0.0899` n `27`; metal avg `-0.0548` n `20`; unknown avg `24.5558` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
