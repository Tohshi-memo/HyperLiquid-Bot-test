# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T15:07:21.674051+00:00`
- Correlation status: `ready`
- Asset price records: `656`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `-0.1145` n `228`; crypto_major avg `-0.0916` n `8`; equity avg `0.1595` n `65`; fx avg `-0.0176` n `5`; index avg `0.0167` n `23`; metal avg `0.0139` n `18`; unknown avg `0.2169` n `375`
- 1h: commodity avg `0.2478` n `12`; crypto_alt avg `0.619` n `228`; crypto_major avg `0.3175` n `8`; equity avg `0.2213` n `65`; fx avg `-0.0086` n `5`; index avg `-0.0259` n `23`; metal avg `0.0324` n `18`; unknown avg `0.2416` n `375`
- 4h: commodity avg `0.4541` n `12`; crypto_alt avg `0.6396` n `228`; crypto_major avg `0.1592` n `8`; equity avg `1.1841` n `65`; fx avg `-0.0472` n `5`; index avg `0.5009` n `23`; metal avg `-0.1528` n `18`; unknown avg `0.3766` n `375`
- 24h: commodity avg `1.7348` n `12`; crypto_alt avg `2.2857` n `228`; crypto_major avg `-0.1439` n `8`; equity avg `1.1234` n `65`; fx avg `0.2033` n `5`; index avg `0.2974` n `23`; metal avg `-0.8178` n `18`; unknown avg `0.3513` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1241`, n `648`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1207`, n `648`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `652`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `648`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0969`, n `648`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `652`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `652`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `652`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `652`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `652`, weak_sample_signal
