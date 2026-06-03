# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T06:07:22.346500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `0.2626` n `228`; crypto_major avg `0.1532` n `8`; equity avg `0.1818` n `72`; fx avg `-0.0202` n `6`; index avg `0.0427` n `23`; metal avg `-0.0459` n `18`; unknown avg `0.0253` n `410`
- 1h: commodity avg `0.1383` n `12`; crypto_alt avg `0.3832` n `228`; crypto_major avg `0.2136` n `8`; equity avg `0.139` n `72`; fx avg `0.034` n `6`; index avg `-0.005` n `23`; metal avg `-0.1648` n `18`; unknown avg `0.31` n `410`
- 4h: commodity avg `0.139` n `12`; crypto_alt avg `1.6902` n `228`; crypto_major avg `1.0271` n `8`; equity avg `0.3683` n `72`; fx avg `0.0539` n `6`; index avg `-0.053` n `23`; metal avg `-0.186` n `18`; unknown avg `0.5667` n `409`
- 24h: commodity avg `1.1541` n `12`; crypto_alt avg `-1.6068` n `228`; crypto_major avg `-3.8744` n `8`; equity avg `1.0796` n `72`; fx avg `0.064` n `6`; index avg `1.1186` n `23`; metal avg `-1.3658` n `18`; unknown avg `-0.8075` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
