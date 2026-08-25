# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T12:07:22.019542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7312` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3212` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0824` n `12`; crypto_alt avg `-0.5087` n `231`; crypto_major avg `-0.4705` n `8`; equity avg `-0.095` n `122`; fx avg `-0.0044` n `6`; index avg `0.0037` n `25`; metal avg `-0.0482` n `20`; unknown avg `-0.1322` n `795`
- 1h: commodity avg `-0.1525` n `12`; crypto_alt avg `-0.8019` n `231`; crypto_major avg `-0.9101` n `8`; equity avg `0.0359` n `122`; fx avg `-0.0127` n `6`; index avg `0.0273` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.1972` n `795`
- 4h: commodity avg `-0.5499` n `12`; crypto_alt avg `-0.8999` n `231`; crypto_major avg `-1.1922` n `8`; equity avg `0.539` n `122`; fx avg `-0.0503` n `6`; index avg `0.129` n `25`; metal avg `0.0233` n `20`; unknown avg `-0.1333` n `794`
- 24h: commodity avg `-0.915` n `12`; crypto_alt avg `-0.9373` n `231`; crypto_major avg `-0.3242` n `8`; equity avg `0.5939` n `122`; fx avg `-0.0005` n `6`; index avg `0.1336` n `25`; metal avg `-0.2755` n `20`; unknown avg `-0.3295` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
