# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T18:22:26.701327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0845` n `12`; crypto_alt avg `-0.1621` n `230`; crypto_major avg `-0.1611` n `8`; equity avg `-0.0666` n `102`; fx avg `-0.0108` n `6`; index avg `0.0045` n `25`; metal avg `-0.003` n `20`; unknown avg `0.0672` n `782`
- 1h: commodity avg `-0.0635` n `12`; crypto_alt avg `-0.4546` n `230`; crypto_major avg `-0.4535` n `8`; equity avg `-0.1395` n `102`; fx avg `-0.0206` n `6`; index avg `-0.0183` n `25`; metal avg `-0.0249` n `20`; unknown avg `0.0651` n `782`
- 4h: commodity avg `0.072` n `12`; crypto_alt avg `-0.6939` n `230`; crypto_major avg `-0.75` n `8`; equity avg `-0.2692` n `102`; fx avg `-0.0156` n `6`; index avg `-0.0277` n `25`; metal avg `-0.0216` n `20`; unknown avg `0.1244` n `782`
- 24h: commodity avg `0.4487` n `12`; crypto_alt avg `-0.8022` n `230`; crypto_major avg `-1.3939` n `8`; equity avg `-1.2716` n `102`; fx avg `-0.1507` n `6`; index avg `-0.1399` n `25`; metal avg `-0.0956` n `20`; unknown avg `4.265` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
