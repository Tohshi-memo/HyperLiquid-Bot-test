# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T07:52:24.820521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `-0.0317` n `8`; equity avg `0.0185` n `112`; fx avg `-0.0009` n `6`; index avg `-0.0037` n `25`; metal avg `0.0118` n `20`; unknown avg `-0.0376` n `784`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `-0.0765` n `8`; equity avg `0.0426` n `112`; fx avg `-0.0075` n `6`; index avg `0.0015` n `25`; metal avg `0.0274` n `20`; unknown avg `0.0733` n `784`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `0.0978` n `230`; crypto_major avg `-0.0054` n `8`; equity avg `-0.05` n `112`; fx avg `-0.008` n `6`; index avg `-0.0436` n `25`; metal avg `0.0112` n `20`; unknown avg `0.0358` n `751`
- 24h: commodity avg `-0.2137` n `12`; crypto_alt avg `-0.0325` n `230`; crypto_major avg `0.6008` n `8`; equity avg `1.1549` n `112`; fx avg `-0.061` n `6`; index avg `0.0782` n `25`; metal avg `0.0632` n `20`; unknown avg `0.1194` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
