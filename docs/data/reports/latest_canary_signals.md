# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T02:37:29.810938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.2106` n `230`; crypto_major avg `-0.2462` n `8`; equity avg `-0.198` n `100`; fx avg `-0.0045` n `6`; index avg `-0.0431` n `25`; metal avg `-0.0596` n `20`; unknown avg `0.1707` n `772`
- 1h: commodity avg `0.0814` n `12`; crypto_alt avg `-0.2266` n `230`; crypto_major avg `-0.3842` n `8`; equity avg `-0.5577` n `100`; fx avg `-0.0276` n `6`; index avg `-0.1612` n `25`; metal avg `-0.0792` n `20`; unknown avg `-0.1317` n `772`
- 4h: commodity avg `-0.0201` n `12`; crypto_alt avg `-0.173` n `230`; crypto_major avg `-0.3852` n `8`; equity avg `-0.6881` n `100`; fx avg `-0.116` n `6`; index avg `-0.2033` n `25`; metal avg `-0.1689` n `20`; unknown avg `-0.4217` n `772`
- 24h: commodity avg `0.5206` n `12`; crypto_alt avg `-1.4138` n `230`; crypto_major avg `-2.1106` n `8`; equity avg `-1.7204` n `99`; fx avg `-0.1184` n `6`; index avg `-0.4828` n `25`; metal avg `-0.9311` n `20`; unknown avg `-0.3733` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0915`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
