# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T11:31:03.666353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `-0.0252` n `228`; crypto_major avg `-0.0403` n `8`; equity avg `0.0114` n `74`; fx avg `0.0` n `6`; index avg `-0.0047` n `23`; metal avg `0.0793` n `18`; unknown avg `0.002` n `644`
- 1h: commodity avg `-0.0499` n `12`; crypto_alt avg `0.3855` n `228`; crypto_major avg `0.3398` n `8`; equity avg `0.0031` n `74`; fx avg `0.0148` n `6`; index avg `0.1266` n `23`; metal avg `0.1149` n `18`; unknown avg `0.2943` n `644`
- 4h: commodity avg `-0.176` n `12`; crypto_alt avg `0.5118` n `228`; crypto_major avg `0.3286` n `8`; equity avg `0.0061` n `74`; fx avg `-0.0039` n `6`; index avg `0.0911` n `23`; metal avg `0.0189` n `18`; unknown avg `0.9436` n `635`
- 24h: commodity avg `-0.0642` n `12`; crypto_alt avg `1.27` n `228`; crypto_major avg `0.3184` n `8`; equity avg `-0.7843` n `74`; fx avg `0.0202` n `6`; index avg `0.648` n `23`; metal avg `0.5057` n `18`; unknown avg `30.523` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
