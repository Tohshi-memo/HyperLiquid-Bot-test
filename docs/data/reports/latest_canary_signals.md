# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T00:07:26.675047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0656` n `230`; crypto_major avg `0.1009` n `8`; equity avg `0.0111` n `100`; fx avg `-0.0143` n `6`; index avg `0.0089` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0719` n `774`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.1003` n `230`; crypto_major avg `-0.0013` n `8`; equity avg `0.072` n `100`; fx avg `0.017` n `6`; index avg `0.0219` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.134` n `774`
- 4h: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.0873` n `230`; crypto_major avg `-0.1107` n `8`; equity avg `0.1331` n `100`; fx avg `-0.0008` n `6`; index avg `0.0376` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.2578` n `774`
- 24h: commodity avg `-0.5973` n `12`; crypto_alt avg `0.408` n `230`; crypto_major avg `1.0172` n `8`; equity avg `0.4373` n `100`; fx avg `-0.0562` n `6`; index avg `0.1296` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.2576` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1233`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1164`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1152`, n `666`, weak_sample_signal
