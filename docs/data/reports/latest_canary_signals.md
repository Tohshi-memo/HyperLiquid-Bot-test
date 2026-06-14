# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T05:03:27.560613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0383` n `228`; crypto_major avg `0.0204` n `8`; equity avg `0.01` n `74`; fx avg `0.0074` n `6`; index avg `-0.0046` n `23`; metal avg `-0.0034` n `18`; unknown avg `-0.2135` n `645`
- 1h: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.4817` n `228`; crypto_major avg `-0.3222` n `8`; equity avg `-0.0741` n `74`; fx avg `-0.0033` n `6`; index avg `-0.0171` n `23`; metal avg `0.0054` n `18`; unknown avg `-0.2185` n `645`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.3986` n `228`; crypto_major avg `-0.3304` n `8`; equity avg `0.0283` n `74`; fx avg `0.0026` n `6`; index avg `-0.0486` n `23`; metal avg `-0.0056` n `18`; unknown avg `-1.5623` n `629`
- 24h: commodity avg `-0.7574` n `12`; crypto_alt avg `1.379` n `228`; crypto_major avg `1.764` n `8`; equity avg `0.7204` n `74`; fx avg `-0.0277` n `6`; index avg `0.3058` n `23`; metal avg `0.3226` n `18`; unknown avg `-1.3002` n `603`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
