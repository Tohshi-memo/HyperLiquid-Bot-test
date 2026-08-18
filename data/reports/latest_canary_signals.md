# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T02:37:27.044117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.225` n `230`; crypto_major avg `-0.1417` n `8`; equity avg `-0.1693` n `114`; fx avg `-0.0112` n `6`; index avg `-0.05` n `25`; metal avg `-0.0357` n `20`; unknown avg `0.0029` n `793`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `-0.5607` n `230`; crypto_major avg `-0.4006` n `8`; equity avg `-1.2832` n `114`; fx avg `-0.0164` n `6`; index avg `-0.202` n `25`; metal avg `-0.2434` n `20`; unknown avg `0.7295` n `793`
- 4h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.6584` n `230`; crypto_major avg `-0.3437` n `8`; equity avg `-1.479` n `114`; fx avg `-0.0654` n `6`; index avg `-0.2475` n `25`; metal avg `-0.1716` n `20`; unknown avg `-0.069` n `793`
- 24h: commodity avg `0.5238` n `12`; crypto_alt avg `-0.8748` n `230`; crypto_major avg `0.1733` n `8`; equity avg `-0.6134` n `114`; fx avg `0.0034` n `6`; index avg `-0.1977` n `25`; metal avg `-0.181` n `20`; unknown avg `0.0901` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
