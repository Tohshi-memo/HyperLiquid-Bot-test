# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T00:52:12.632304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.2621` n `228`; crypto_major avg `-0.1851` n `8`; equity avg `-0.0083` n `65`; fx avg `0.0002` n `5`; index avg `0.0055` n `23`; metal avg `-0.0134` n `18`; unknown avg `0.0177` n `376`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `-0.4124` n `228`; crypto_major avg `-0.2471` n `8`; equity avg `-0.0038` n `65`; fx avg `-0.0091` n `5`; index avg `0.0114` n `23`; metal avg `0.0256` n `18`; unknown avg `-0.1334` n `376`
- 4h: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.7004` n `228`; crypto_major avg `-0.3722` n `8`; equity avg `0.2048` n `65`; fx avg `-0.0287` n `5`; index avg `0.0841` n `23`; metal avg `0.0876` n `18`; unknown avg `-0.2858` n `376`
- 24h: commodity avg `0.5044` n `12`; crypto_alt avg `-1.1919` n `228`; crypto_major avg `-0.2468` n `8`; equity avg `0.748` n `65`; fx avg `-0.0136` n `5`; index avg `0.4831` n `23`; metal avg `0.3323` n `18`; unknown avg `-0.1741` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
