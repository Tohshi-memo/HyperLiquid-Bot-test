# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T20:52:19.550453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0617` n `12`; crypto_alt avg `-0.0077` n `228`; crypto_major avg `-0.0402` n `8`; equity avg `-0.0201` n `66`; fx avg `-0.0311` n `6`; index avg `-0.0089` n `23`; metal avg `-0.0533` n `18`; unknown avg `0.0306` n `383`
- 1h: commodity avg `-0.0548` n `12`; crypto_alt avg `0.2405` n `228`; crypto_major avg `0.0005` n `8`; equity avg `-0.0475` n `66`; fx avg `-0.0338` n `6`; index avg `-0.0644` n `23`; metal avg `-0.141` n `18`; unknown avg `0.2707` n `383`
- 4h: commodity avg `0.3149` n `12`; crypto_alt avg `-0.0993` n `228`; crypto_major avg `-0.1882` n `8`; equity avg `-0.2337` n `66`; fx avg `0.0526` n `6`; index avg `-0.2084` n `23`; metal avg `-0.5498` n `18`; unknown avg `1.2061` n `383`
- 24h: commodity avg `1.1696` n `12`; crypto_alt avg `0.2955` n `228`; crypto_major avg `0.3023` n `8`; equity avg `0.1079` n `66`; fx avg `0.0554` n `6`; index avg `-0.5528` n `23`; metal avg `-2.7044` n `18`; unknown avg `0.9305` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
