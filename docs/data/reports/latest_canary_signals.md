# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T04:22:27.257804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.841` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5109` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.374` n `228`; crypto_major avg `0.13` n `8`; equity avg `0.1798` n `74`; fx avg `-0.0225` n `6`; index avg `0.1311` n `23`; metal avg `-0.0347` n `18`; unknown avg `0.1198` n `517`
- 1h: commodity avg `0.024` n `12`; crypto_alt avg `0.3065` n `228`; crypto_major avg `-0.1908` n `8`; equity avg `0.5025` n `74`; fx avg `-0.0235` n `6`; index avg `0.296` n `23`; metal avg `0.114` n `18`; unknown avg `-0.2605` n `517`
- 4h: commodity avg `-0.1453` n `12`; crypto_alt avg `-1.1396` n `228`; crypto_major avg `-0.8719` n `8`; equity avg `0.9691` n `74`; fx avg `-0.1321` n `6`; index avg `0.639` n `23`; metal avg `0.1977` n `18`; unknown avg `-0.3799` n `517`
- 24h: commodity avg `-1.1164` n `12`; crypto_alt avg `-0.2335` n `228`; crypto_major avg `0.3638` n `8`; equity avg `2.0463` n `74`; fx avg `-0.313` n `6`; index avg `1.0233` n `23`; metal avg `0.0099` n `18`; unknown avg `-3.1474` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
