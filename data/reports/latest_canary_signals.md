# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T13:22:13.370039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.2705` n `228`; crypto_major avg `-0.3452` n `8`; equity avg `-0.0422` n `65`; fx avg `0.0` n `5`; index avg `0.0155` n `23`; metal avg `0.0086` n `18`; unknown avg `0.0021` n `383`
- 1h: commodity avg `0.0443` n `12`; crypto_alt avg `-0.3845` n `228`; crypto_major avg `-0.347` n `8`; equity avg `0.0944` n `65`; fx avg `-0.0017` n `5`; index avg `0.0822` n `23`; metal avg `0.0267` n `18`; unknown avg `-0.0956` n `383`
- 4h: commodity avg `0.0415` n `12`; crypto_alt avg `-0.5228` n `228`; crypto_major avg `0.0013` n `8`; equity avg `0.266` n `65`; fx avg `-0.0156` n `5`; index avg `0.1264` n `23`; metal avg `0.0052` n `18`; unknown avg `-0.1084` n `383`
- 24h: commodity avg `1.8153` n `12`; crypto_alt avg `-9.3374` n `228`; crypto_major avg `-2.5385` n `8`; equity avg `-2.5677` n `65`; fx avg `-0.1861` n `5`; index avg `-1.634` n `23`; metal avg `-5.8316` n `18`; unknown avg `550.0199` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
