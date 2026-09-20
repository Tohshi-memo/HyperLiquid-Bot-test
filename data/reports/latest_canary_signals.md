# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T20:37:31.153485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1049` n `234`; crypto_major avg `-0.0602` n `8`; equity avg `0.0329` n `140`; fx avg `0.0112` n `6`; index avg `0.0314` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.2542` n `913`
- 1h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.4213` n `234`; crypto_major avg `-0.238` n `8`; equity avg `0.0502` n `140`; fx avg `0.0039` n `6`; index avg `0.0236` n `26`; metal avg `-0.0092` n `20`; unknown avg `7.2507` n `905`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `0.8469` n `234`; crypto_major avg `-0.0172` n `8`; equity avg `0.0417` n `140`; fx avg `-0.0132` n `6`; index avg `0.0234` n `26`; metal avg `-0.0302` n `20`; unknown avg `2.678` n `885`
- 24h: commodity avg `0.3622` n `12`; crypto_alt avg `0.7743` n `234`; crypto_major avg `-0.3679` n `8`; equity avg `-0.0686` n `140`; fx avg `0.0176` n `6`; index avg `-0.0119` n `26`; metal avg `-0.0452` n `20`; unknown avg `3.4128` n `797`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
