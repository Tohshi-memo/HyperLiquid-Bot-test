# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T23:22:15.665010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0576` n `12`; crypto_alt avg `-0.0737` n `228`; crypto_major avg `0.0072` n `8`; equity avg `-0.0104` n `66`; fx avg `-0.0009` n `5`; index avg `-0.0253` n `23`; metal avg `-0.0283` n `18`; unknown avg `-0.1908` n `383`
- 1h: commodity avg `0.2282` n `12`; crypto_alt avg `-0.5755` n `228`; crypto_major avg `-0.5033` n `8`; equity avg `-0.0646` n `66`; fx avg `-0.0015` n `5`; index avg `-0.1102` n `23`; metal avg `0.2217` n `18`; unknown avg `-0.0723` n `383`
- 4h: commodity avg `0.0595` n `12`; crypto_alt avg `-0.7795` n `228`; crypto_major avg `-0.499` n `8`; equity avg `0.1504` n `66`; fx avg `-0.0203` n `5`; index avg `0.0242` n `23`; metal avg `0.5713` n `18`; unknown avg `-0.2253` n `383`
- 24h: commodity avg `1.946` n `12`; crypto_alt avg `-9.9731` n `228`; crypto_major avg `-2.1172` n `8`; equity avg `-2.5798` n `65`; fx avg `-0.1748` n `5`; index avg `-1.5643` n `23`; metal avg `-5.4191` n `18`; unknown avg `550.5538` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
