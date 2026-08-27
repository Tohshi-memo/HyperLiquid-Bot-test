# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T09:52:26.440600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.2042` n `231`; crypto_major avg `-0.102` n `8`; equity avg `0.0469` n `127`; fx avg `0.0064` n `6`; index avg `0.003` n `26`; metal avg `0.031` n `20`; unknown avg `0.0413` n `792`
- 1h: commodity avg `0.1411` n `12`; crypto_alt avg `-0.1097` n `231`; crypto_major avg `0.1933` n `8`; equity avg `-0.055` n `127`; fx avg `0.0215` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0489` n `20`; unknown avg `0.0419` n `792`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `1.5288` n `231`; crypto_major avg `1.595` n `8`; equity avg `0.8718` n `127`; fx avg `-0.0014` n `6`; index avg `0.1024` n `26`; metal avg `-0.1072` n `20`; unknown avg `0.2321` n `775`
- 24h: commodity avg `0.5348` n `12`; crypto_alt avg `2.3963` n `231`; crypto_major avg `3.021` n `8`; equity avg `2.1084` n `127`; fx avg `-0.0791` n `6`; index avg `0.3159` n `26`; metal avg `-0.3905` n `20`; unknown avg `0.5994` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
