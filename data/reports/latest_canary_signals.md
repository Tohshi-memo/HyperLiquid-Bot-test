# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T02:07:26.920308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.0541` n `230`; crypto_major avg `0.0258` n `8`; equity avg `0.007` n `100`; fx avg `-0.005` n `6`; index avg `-0.0028` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0556` n `774`
- 1h: commodity avg `0.0368` n `12`; crypto_alt avg `-0.2529` n `230`; crypto_major avg `-0.0265` n `8`; equity avg `-0.0425` n `100`; fx avg `-0.0166` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.0414` n `774`
- 4h: commodity avg `-0.0585` n `12`; crypto_alt avg `0.2071` n `230`; crypto_major avg `0.3054` n `8`; equity avg `-0.0499` n `100`; fx avg `0.0284` n `6`; index avg `0.0191` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.1853` n `774`
- 24h: commodity avg `-0.2835` n `12`; crypto_alt avg `-1.0432` n `230`; crypto_major avg `-0.8222` n `8`; equity avg `-2.8885` n `100`; fx avg `-0.0327` n `6`; index avg `-0.2807` n `25`; metal avg `0.0958` n `20`; unknown avg `14.0187` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1224`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1157`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1072`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1066`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
