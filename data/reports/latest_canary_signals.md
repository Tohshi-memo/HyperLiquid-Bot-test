# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T20:52:28.899410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `-0.1294` n `230`; crypto_major avg `-0.0718` n `8`; equity avg `0.0045` n `100`; fx avg `-0.0005` n `6`; index avg `0.0063` n `25`; metal avg `0.0007` n `20`; unknown avg `0.0609` n `774`
- 1h: commodity avg `0.2629` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `-0.0297` n `8`; equity avg `0.2622` n `100`; fx avg `-0.0164` n `6`; index avg `0.0206` n `25`; metal avg `0.0081` n `20`; unknown avg `0.0808` n `773`
- 4h: commodity avg `0.3841` n `12`; crypto_alt avg `0.1414` n `230`; crypto_major avg `0.2234` n `8`; equity avg `-0.8715` n `100`; fx avg `-0.0258` n `6`; index avg `-0.1568` n `25`; metal avg `-0.1095` n `20`; unknown avg `-0.0244` n `773`
- 24h: commodity avg `-0.2817` n `12`; crypto_alt avg `-1.2318` n `230`; crypto_major avg `-1.1181` n `8`; equity avg `-3.4918` n `100`; fx avg `-0.1795` n `6`; index avg `-0.5019` n `25`; metal avg `-0.0071` n `20`; unknown avg `13.8675` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1272`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1239`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1104`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `666`, weak_sample_signal
