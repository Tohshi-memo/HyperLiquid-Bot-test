# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T10:52:27.449423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1809` n `13`; crypto_alt avg `0.4754` n `238`; crypto_major avg `0.4429` n `8`; equity avg `0.4485` n `154`; fx avg `-0.0117` n `6`; index avg `0.0732` n `27`; metal avg `0.0753` n `20`; unknown avg `1.5755` n `1238`
- 1h: commodity avg `-0.1761` n `13`; crypto_alt avg `0.4797` n `238`; crypto_major avg `0.4913` n `8`; equity avg `0.3627` n `154`; fx avg `0.0086` n `6`; index avg `0.06` n `27`; metal avg `0.0648` n `20`; unknown avg `2.8915` n `1234`
- 4h: commodity avg `-0.155` n `13`; crypto_alt avg `0.2881` n `238`; crypto_major avg `0.4675` n `8`; equity avg `0.8689` n `154`; fx avg `-0.0137` n `6`; index avg `0.1335` n `27`; metal avg `0.1254` n `20`; unknown avg `73.082` n `1190`
- 24h: commodity avg `-0.0299` n `13`; crypto_alt avg `-0.3455` n `237`; crypto_major avg `-0.087` n `8`; equity avg `1.272` n `153`; fx avg `-0.0422` n `6`; index avg `0.403` n `27`; metal avg `-0.2332` n `20`; unknown avg `1049.8121` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
