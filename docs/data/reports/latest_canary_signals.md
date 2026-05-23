# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T11:22:14.152094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.0013` n `228`; crypto_major avg `0.0583` n `8`; equity avg `0.0217` n `67`; fx avg `0.0002` n `6`; index avg `0.0353` n `23`; metal avg `0.0381` n `18`; unknown avg `0.0629` n `396`
- 1h: commodity avg `0.1296` n `12`; crypto_alt avg `0.0366` n `228`; crypto_major avg `0.1108` n `8`; equity avg `0.0305` n `67`; fx avg `0.0015` n `6`; index avg `0.1465` n `23`; metal avg `0.0202` n `18`; unknown avg `0.0547` n `396`
- 4h: commodity avg `0.0793` n `12`; crypto_alt avg `-1.4073` n `228`; crypto_major avg `-0.7898` n `8`; equity avg `-0.1033` n `67`; fx avg `-0.0264` n `6`; index avg `-0.0862` n `23`; metal avg `-0.1094` n `18`; unknown avg `-0.0722` n `386`
- 24h: commodity avg `-0.3423` n `12`; crypto_alt avg `-5.3434` n `228`; crypto_major avg `-3.7823` n `8`; equity avg `-1.477` n `67`; fx avg `0.0607` n `6`; index avg `-0.1079` n `23`; metal avg `-0.6572` n `18`; unknown avg `-2.2018` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
