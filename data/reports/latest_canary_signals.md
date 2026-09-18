# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T20:52:38.281187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `12`; crypto_alt avg `0.14` n `234`; crypto_major avg `0.2183` n `8`; equity avg `0.0461` n `140`; fx avg `0.012` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0275` n `20`; unknown avg `5.2547` n `942`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.3068` n `234`; crypto_major avg `-0.1961` n `8`; equity avg `0.1856` n `140`; fx avg `0.0196` n `6`; index avg `0.0412` n `26`; metal avg `-0.0153` n `20`; unknown avg `65.1997` n `896`
- 4h: commodity avg `-0.0802` n `12`; crypto_alt avg `1.4107` n `234`; crypto_major avg `0.9755` n `8`; equity avg `0.8004` n `140`; fx avg `0.0384` n `6`; index avg `0.1743` n `26`; metal avg `-0.0422` n `20`; unknown avg `6.0778` n `878`
- 24h: commodity avg `-0.0637` n `12`; crypto_alt avg `6.9212` n `234`; crypto_major avg `7.0265` n `8`; equity avg `1.3294` n `140`; fx avg `0.2294` n `6`; index avg `0.0586` n `26`; metal avg `0.3901` n `20`; unknown avg `9.9581` n `727`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
