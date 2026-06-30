# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T06:07:30.580230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `0.0885` n `228`; crypto_major avg `-0.0239` n `8`; equity avg `-0.0411` n `88`; fx avg `0.009` n `6`; index avg `-0.0189` n `23`; metal avg `0.0596` n `20`; unknown avg `-0.0382` n `739`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0057` n `228`; crypto_major avg `-0.0012` n `8`; equity avg `-0.1906` n `88`; fx avg `0.0284` n `6`; index avg `-0.0719` n `23`; metal avg `-0.0648` n `20`; unknown avg `-0.4041` n `737`
- 4h: commodity avg `-0.0956` n `12`; crypto_alt avg `0.0591` n `228`; crypto_major avg `-0.2452` n `8`; equity avg `0.4704` n `88`; fx avg `-0.0256` n `6`; index avg `0.1352` n `23`; metal avg `0.1097` n `20`; unknown avg `8.7556` n `737`
- 24h: commodity avg `-0.2296` n `12`; crypto_alt avg `-0.2294` n `228`; crypto_major avg `0.5929` n `8`; equity avg `2.0027` n `88`; fx avg `0.1755` n `6`; index avg `0.2572` n `23`; metal avg `-0.6668` n `20`; unknown avg `10.6929` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
