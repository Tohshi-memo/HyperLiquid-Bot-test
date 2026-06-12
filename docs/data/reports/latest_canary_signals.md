# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T01:52:26.514295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.154` n `12`; crypto_alt avg `0.096` n `228`; crypto_major avg `0.04` n `8`; equity avg `0.1843` n `74`; fx avg `0.0022` n `6`; index avg `0.1101` n `23`; metal avg `0.2232` n `18`; unknown avg `0.1007` n `557`
- 1h: commodity avg `0.2766` n `12`; crypto_alt avg `-0.4642` n `228`; crypto_major avg `-0.5543` n `8`; equity avg `-0.5341` n `74`; fx avg `0.0286` n `6`; index avg `-0.1474` n `23`; metal avg `-0.0966` n `18`; unknown avg `0.2153` n `556`
- 4h: commodity avg `0.3292` n `12`; crypto_alt avg `-0.422` n `228`; crypto_major avg `-0.4644` n `8`; equity avg `0.3699` n `74`; fx avg `0.015` n `6`; index avg `0.0889` n `23`; metal avg `0.0486` n `18`; unknown avg `-0.0356` n `556`
- 24h: commodity avg `-2.2153` n `12`; crypto_alt avg `2.3678` n `228`; crypto_major avg `2.208` n `8`; equity avg `3.6129` n `74`; fx avg `-0.0343` n `6`; index avg `2.0035` n `23`; metal avg `2.5913` n `18`; unknown avg `2.2962` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
