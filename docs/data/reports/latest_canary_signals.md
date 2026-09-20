# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T14:52:26.317772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `0.057` n `234`; crypto_major avg `0.0456` n `8`; equity avg `0.0144` n `140`; fx avg `0.0343` n `6`; index avg `0.0104` n `26`; metal avg `-0.0029` n `20`; unknown avg `-0.2415` n `943`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `0.2051` n `234`; crypto_major avg `0.1476` n `8`; equity avg `0.0048` n `140`; fx avg `0.0214` n `6`; index avg `0.0044` n `26`; metal avg `0.0005` n `20`; unknown avg `1.217` n `941`
- 4h: commodity avg `0.0455` n `12`; crypto_alt avg `0.3442` n `234`; crypto_major avg `0.3247` n `8`; equity avg `0.0167` n `140`; fx avg `0.0059` n `6`; index avg `0.0129` n `26`; metal avg `-0.009` n `20`; unknown avg `1.5272` n `935`
- 24h: commodity avg `0.3619` n `12`; crypto_alt avg `-2.2624` n `234`; crypto_major avg `-2.3211` n `8`; equity avg `-0.3085` n `140`; fx avg `-0.0389` n `6`; index avg `-0.0447` n `26`; metal avg `-0.0437` n `20`; unknown avg `1.1981` n `818`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
