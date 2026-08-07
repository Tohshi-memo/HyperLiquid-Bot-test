# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T23:52:23.343713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.0405` n `230`; crypto_major avg `0.025` n `8`; equity avg `0.0758` n `112`; fx avg `-0.0021` n `6`; index avg `0.0018` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.0926` n `783`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0432` n `230`; crypto_major avg `0.0149` n `8`; equity avg `0.0651` n `112`; fx avg `-0.0068` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.2326` n `782`
- 4h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.3729` n `230`; crypto_major avg `-0.2435` n `8`; equity avg `0.27` n `112`; fx avg `0.0382` n `6`; index avg `-0.0109` n `25`; metal avg `0.0427` n `20`; unknown avg `-0.1922` n `782`
- 24h: commodity avg `-0.1743` n `12`; crypto_alt avg `-0.3157` n `230`; crypto_major avg `-0.04` n `8`; equity avg `1.6973` n `112`; fx avg `-0.1249` n `6`; index avg `0.0792` n `25`; metal avg `0.4129` n `20`; unknown avg `0.0648` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
