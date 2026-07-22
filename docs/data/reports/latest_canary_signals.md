# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T02:07:33.318264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `5`; crypto_alt avg `-0.1308` n `225`; crypto_major avg `-0.2169` n `7`; equity avg `-0.3608` n `8`; fx avg `0.0135` n `1`; index avg `-0.0845` n `4`; metal avg `-0.0064` n `20`; unknown avg `0.1157` n `900`
- 1h: commodity avg `0.0` n `5`; crypto_alt avg `-0.1009` n `225`; crypto_major avg `-0.1949` n `7`; equity avg `-0.079` n `8`; fx avg `0.0541` n `1`; index avg `0.1211` n `4`; metal avg `0.0962` n `20`; unknown avg `0.0143` n `900`
- 4h: commodity avg `0.0` n `5`; crypto_alt avg `-0.0162` n `225`; crypto_major avg `0.1877` n `7`; equity avg `-0.2241` n `8`; fx avg `-0.0203` n `1`; index avg `0.1473` n `4`; metal avg `0.4539` n `20`; unknown avg `-0.1538` n `900`
- 24h: commodity avg `0.0` n `5`; crypto_alt avg `0.7302` n `225`; crypto_major avg `0.6068` n `7`; equity avg `4.8008` n `8`; fx avg `0.0608` n `1`; index avg `2.6816` n `4`; metal avg `1.1041` n `20`; unknown avg `0.7768` n `884`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0681`, n `664`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0561`, n `664`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0485`, n `664`, weak_sample_signal
