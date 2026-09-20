# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T13:22:27.677108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.2838` n `234`; crypto_major avg `-0.1522` n `8`; equity avg `-0.0065` n `140`; fx avg `-0.0053` n `6`; index avg `0.0043` n `26`; metal avg `0.0027` n `20`; unknown avg `0.0397` n `943`
- 1h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1506` n `234`; crypto_major avg `-0.0516` n `8`; equity avg `0.0062` n `140`; fx avg `-0.005` n `6`; index avg `0.0091` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.1923` n `941`
- 4h: commodity avg `0.0683` n `12`; crypto_alt avg `-0.4275` n `234`; crypto_major avg `-0.0272` n `8`; equity avg `0.0315` n `140`; fx avg `-0.0149` n `6`; index avg `0.0256` n `26`; metal avg `-0.0367` n `20`; unknown avg `0.2311` n `935`
- 24h: commodity avg `0.2839` n `12`; crypto_alt avg `-2.1957` n `234`; crypto_major avg `-2.3768` n `8`; equity avg `-0.2471` n `140`; fx avg `-0.0491` n `6`; index avg `-0.0424` n `26`; metal avg `-0.0256` n `20`; unknown avg `0.5692` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
