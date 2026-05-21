# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T00:37:21.925167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2037` n `12`; crypto_alt avg `0.2729` n `228`; crypto_major avg `0.1846` n `8`; equity avg `0.155` n `66`; fx avg `-0.0048` n `6`; index avg `0.1041` n `23`; metal avg `0.1328` n `18`; unknown avg `0.1688` n `384`
- 1h: commodity avg `0.1422` n `12`; crypto_alt avg `0.5332` n `228`; crypto_major avg `0.6075` n `8`; equity avg `0.3505` n `66`; fx avg `0.031` n `6`; index avg `0.1406` n `23`; metal avg `0.0196` n `18`; unknown avg `2.3816` n `384`
- 4h: commodity avg `0.1647` n `12`; crypto_alt avg `0.4148` n `228`; crypto_major avg `0.9836` n `8`; equity avg `0.1629` n `66`; fx avg `0.0324` n `6`; index avg `-0.0762` n `23`; metal avg `-0.094` n `18`; unknown avg `2.6067` n `384`
- 24h: commodity avg `-2.1167` n `12`; crypto_alt avg `3.4858` n `228`; crypto_major avg `3.3625` n `8`; equity avg `1.947` n `66`; fx avg `-0.0697` n `6`; index avg `1.1516` n `23`; metal avg `1.0638` n `18`; unknown avg `4.063` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
