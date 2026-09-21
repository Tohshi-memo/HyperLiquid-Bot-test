# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T06:07:31.022287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.046` n `12`; crypto_alt avg `0.0229` n `234`; crypto_major avg `-0.0304` n `8`; equity avg `0.0129` n `140`; fx avg `0.0003` n `6`; index avg `0.0125` n `26`; metal avg `0.0109` n `20`; unknown avg `2.9088` n `910`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `0.0283` n `234`; crypto_major avg `0.2509` n `8`; equity avg `0.0725` n `140`; fx avg `-0.0137` n `6`; index avg `0.0253` n `26`; metal avg `-0.0143` n `20`; unknown avg `2.999` n `910`
- 4h: commodity avg `0.0984` n `12`; crypto_alt avg `1.4675` n `234`; crypto_major avg `0.5225` n `8`; equity avg `0.0082` n `140`; fx avg `-0.0259` n `6`; index avg `0.0467` n `26`; metal avg `-0.1159` n `20`; unknown avg `45.1764` n `904`
- 24h: commodity avg `-0.543` n `12`; crypto_alt avg `3.3018` n `234`; crypto_major avg `2.6982` n `8`; equity avg `1.0728` n `140`; fx avg `-0.0287` n `6`; index avg `0.2312` n `26`; metal avg `-0.0119` n `20`; unknown avg `3.8285` n `773`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
