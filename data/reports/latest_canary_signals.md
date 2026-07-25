# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T01:07:31.552750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0719` n `12`; crypto_alt avg `0.2067` n `230`; crypto_major avg `0.1193` n `8`; equity avg `0.0739` n `100`; fx avg `0.0172` n `6`; index avg `0.0163` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0498` n `774`
- 1h: commodity avg `-0.012` n `12`; crypto_alt avg `0.1928` n `230`; crypto_major avg `0.055` n `8`; equity avg `-0.0146` n `100`; fx avg `-0.0107` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0249` n `774`
- 4h: commodity avg `-0.1005` n `12`; crypto_alt avg `0.2998` n `230`; crypto_major avg `0.1526` n `8`; equity avg `-0.0311` n `100`; fx avg `0.0519` n `6`; index avg `0.0263` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.2736` n `774`
- 24h: commodity avg `-0.2716` n `12`; crypto_alt avg `-0.5717` n `230`; crypto_major avg `-0.7093` n `8`; equity avg `-2.9519` n `100`; fx avg `-0.0434` n `6`; index avg `-0.3294` n `25`; metal avg `0.0661` n `20`; unknown avg `14.0328` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.125`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.117`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1093`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1075`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
