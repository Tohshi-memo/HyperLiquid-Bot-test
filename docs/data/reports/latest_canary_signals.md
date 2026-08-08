# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T03:22:31.046984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `0.0683` n `230`; crypto_major avg `0.0791` n `8`; equity avg `0.037` n `112`; fx avg `0.0006` n `6`; index avg `-0.0016` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0246` n `783`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `0.0794` n `230`; crypto_major avg `0.1737` n `8`; equity avg `-0.0389` n `112`; fx avg `-0.0011` n `6`; index avg `0.0003` n `25`; metal avg `0.0145` n `20`; unknown avg `0.1525` n `783`
- 4h: commodity avg `0.0019` n `12`; crypto_alt avg `0.2543` n `230`; crypto_major avg `0.3153` n `8`; equity avg `0.1308` n `112`; fx avg `-0.0042` n `6`; index avg `-0.0049` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.1516` n `783`
- 24h: commodity avg `-0.1791` n `12`; crypto_alt avg `-0.161` n `230`; crypto_major avg `0.3274` n `8`; equity avg `1.7535` n `112`; fx avg `-0.09` n `6`; index avg `0.2385` n `25`; metal avg `0.3716` n `20`; unknown avg `-0.0038` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
