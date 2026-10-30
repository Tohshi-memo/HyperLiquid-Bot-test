# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T07:37:31.951446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.07` n `13`; crypto_alt avg `-0.0498` n `238`; crypto_major avg `-0.4558` n `8`; equity avg `-0.0787` n `156`; fx avg `0.0216` n `6`; index avg `-0.005` n `27`; metal avg `-0.0381` n `20`; unknown avg `0.0093` n `1258`
- 1h: commodity avg `0.1985` n `13`; crypto_alt avg `-0.2823` n `238`; crypto_major avg `-0.7609` n `8`; equity avg `-0.3718` n `156`; fx avg `0.0172` n `6`; index avg `0.0093` n `27`; metal avg `-0.0973` n `20`; unknown avg `131.2935` n `1252`
- 4h: commodity avg `0.0617` n `13`; crypto_alt avg `1.331` n `238`; crypto_major avg `0.2954` n `8`; equity avg `-0.0717` n `156`; fx avg `-0.005` n `6`; index avg `0.0835` n `27`; metal avg `-0.208` n `20`; unknown avg `2.515` n `1216`
- 24h: commodity avg `-0.0372` n `13`; crypto_alt avg `-2.8584` n `238`; crypto_major avg `-0.1129` n `8`; equity avg `-2.7226` n `155`; fx avg `0.1039` n `6`; index avg `-0.2894` n `27`; metal avg `-0.721` n `20`; unknown avg `31.9337` n `978`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
