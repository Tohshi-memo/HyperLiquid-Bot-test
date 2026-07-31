# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T11:07:29.878941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `0.0543` n `230`; crypto_major avg `0.0927` n `8`; equity avg `0.3115` n `102`; fx avg `0.0189` n `6`; index avg `0.0156` n `25`; metal avg `-0.0306` n `20`; unknown avg `1.9962` n `780`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `0.2219` n `230`; crypto_major avg `0.3251` n `8`; equity avg `0.3966` n `102`; fx avg `0.0284` n `6`; index avg `0.0657` n `25`; metal avg `0.0053` n `20`; unknown avg `2.6943` n `780`
- 4h: commodity avg `0.3385` n `12`; crypto_alt avg `-0.0343` n `230`; crypto_major avg `-0.3183` n `8`; equity avg `0.8767` n `102`; fx avg `0.0613` n `6`; index avg `0.0816` n `25`; metal avg `-0.1178` n `20`; unknown avg `0.2454` n `779`
- 24h: commodity avg `0.279` n `12`; crypto_alt avg `-0.0642` n `230`; crypto_major avg `-0.0523` n `8`; equity avg `7.6256` n `102`; fx avg `-0.0628` n `6`; index avg `1.0907` n `25`; metal avg `0.0354` n `20`; unknown avg `0.2845` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
