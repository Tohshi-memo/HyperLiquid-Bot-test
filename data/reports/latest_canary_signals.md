# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T02:37:26.826268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0645` n `12`; crypto_alt avg `-0.5564` n `234`; crypto_major avg `-0.2348` n `8`; equity avg `-0.0649` n `140`; fx avg `-0.0108` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.2363` n `943`
- 1h: commodity avg `0.1314` n `12`; crypto_alt avg `-0.055` n `234`; crypto_major avg `-0.1847` n `8`; equity avg `-0.0048` n `140`; fx avg `0.0081` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0122` n `20`; unknown avg `1.7603` n `941`
- 4h: commodity avg `0.2564` n `12`; crypto_alt avg `0.1108` n `234`; crypto_major avg `-0.4978` n `8`; equity avg `0.0018` n `140`; fx avg `-0.0001` n `6`; index avg `-0.0191` n `26`; metal avg `-0.001` n `20`; unknown avg `2.2805` n `919`
- 24h: commodity avg `0.1675` n `12`; crypto_alt avg `0.0027` n `234`; crypto_major avg `-1.5636` n `8`; equity avg `0.0875` n `140`; fx avg `-0.0592` n `6`; index avg `0.0201` n `26`; metal avg `0.0185` n `20`; unknown avg `1.3968` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
