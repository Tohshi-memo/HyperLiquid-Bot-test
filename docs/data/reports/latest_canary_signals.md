# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T06:07:15.682976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0787` n `12`; crypto_alt avg `0.0645` n `228`; crypto_major avg `0.0163` n `8`; equity avg `0.0604` n `66`; fx avg `0.0139` n `6`; index avg `-0.0178` n `23`; metal avg `0.1657` n `18`; unknown avg `0.2587` n `375`
- 1h: commodity avg `0.0696` n `12`; crypto_alt avg `-0.5581` n `228`; crypto_major avg `-0.2042` n `8`; equity avg `-0.1703` n `66`; fx avg `0.0359` n `6`; index avg `-0.0231` n `23`; metal avg `-0.1502` n `18`; unknown avg `0.0672` n `374`
- 4h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.2776` n `228`; crypto_major avg `0.1981` n `8`; equity avg `0.1872` n `66`; fx avg `0.05` n `6`; index avg `0.1414` n `23`; metal avg `-0.7498` n `18`; unknown avg `1.6596` n `374`
- 24h: commodity avg `-2.3067` n `12`; crypto_alt avg `2.1848` n `228`; crypto_major avg `3.0469` n `8`; equity avg `2.3359` n `66`; fx avg `0.0644` n `6`; index avg `1.6502` n `23`; metal avg `0.9601` n `18`; unknown avg `5.7699` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
