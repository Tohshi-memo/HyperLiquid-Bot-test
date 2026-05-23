# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T09:52:15.794302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1175` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.0297` n `228`; crypto_major avg `0.0048` n `8`; equity avg `-0.0126` n `67`; fx avg `0.0` n `6`; index avg `0.0061` n `23`; metal avg `-0.018` n `18`; unknown avg `0.8579` n `396`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `0.1461` n `228`; crypto_major avg `0.0077` n `8`; equity avg `0.0947` n `67`; fx avg `0.0065` n `6`; index avg `0.0249` n `23`; metal avg `-0.0294` n `18`; unknown avg `0.2351` n `396`
- 4h: commodity avg `-0.0383` n `12`; crypto_alt avg `-1.7458` n `228`; crypto_major avg `-1.1968` n `8`; equity avg `-0.1497` n `67`; fx avg `-0.0279` n `6`; index avg `-0.0793` n `23`; metal avg `-0.0034` n `18`; unknown avg `0.7767` n `376`
- 24h: commodity avg `-0.3942` n `12`; crypto_alt avg `-5.6195` n `228`; crypto_major avg `-3.9309` n `8`; equity avg `-1.7624` n `67`; fx avg `0.0303` n `6`; index avg `-0.1878` n `23`; metal avg `-0.8923` n `18`; unknown avg `-1.3525` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
