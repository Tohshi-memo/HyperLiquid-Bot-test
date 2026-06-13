# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T20:00:20.484380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.2164` n `228`; crypto_major avg `-0.1164` n `8`; equity avg `0.0058` n `74`; fx avg `-0.0001` n `6`; index avg `0.2395` n `23`; metal avg `0.2213` n `18`; unknown avg `0.0582` n `644`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `0.1852` n `228`; crypto_major avg `0.0661` n `8`; equity avg `0.1106` n `74`; fx avg `-0.0076` n `6`; index avg `0.2202` n `23`; metal avg `0.0194` n `18`; unknown avg `-0.4179` n `644`
- 4h: commodity avg `-0.1599` n `12`; crypto_alt avg `-0.0734` n `228`; crypto_major avg `-0.0872` n `8`; equity avg `0.147` n `74`; fx avg `0.0245` n `6`; index avg `0.1335` n `23`; metal avg `0.1205` n `18`; unknown avg `-0.3835` n `644`
- 24h: commodity avg `-0.7858` n `12`; crypto_alt avg `2.0456` n `228`; crypto_major avg `0.579` n `8`; equity avg `0.5615` n `74`; fx avg `0.0516` n `6`; index avg `0.7431` n `23`; metal avg `0.3577` n `18`; unknown avg `-1.6947` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
