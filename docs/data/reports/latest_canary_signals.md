# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T15:22:18.253154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8918` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1095` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2305` n `12`; crypto_alt avg `-0.3653` n `228`; crypto_major avg `-0.3514` n `8`; equity avg `0.0077` n `67`; fx avg `0.0196` n `6`; index avg `0.1548` n `23`; metal avg `-0.0886` n `18`; unknown avg `0.8809` n `419`
- 1h: commodity avg `0.7013` n `12`; crypto_alt avg `-0.3605` n `228`; crypto_major avg `-0.3136` n `8`; equity avg `0.9135` n `67`; fx avg `-0.0012` n `6`; index avg `0.6567` n `23`; metal avg `0.3095` n `18`; unknown avg `0.8931` n `419`
- 4h: commodity avg `0.3255` n `12`; crypto_alt avg `-0.2978` n `228`; crypto_major avg `0.101` n `8`; equity avg `1.9928` n `67`; fx avg `0.0829` n `6`; index avg `1.2105` n `23`; metal avg `1.2529` n `18`; unknown avg `0.6657` n `419`
- 24h: commodity avg `0.4201` n `12`; crypto_alt avg `-6.1292` n `228`; crypto_major avg `-3.3871` n `8`; equity avg `1.308` n `67`; fx avg `0.0169` n `6`; index avg `0.9796` n `23`; metal avg `0.1381` n `18`; unknown avg `-0.6958` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
