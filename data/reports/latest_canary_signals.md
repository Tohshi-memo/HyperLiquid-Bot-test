# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T12:22:17.863812+00:00`
- Correlation status: `ready`
- Asset price records: `645`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1144` n `12`; crypto_alt avg `-0.0768` n `228`; crypto_major avg `-0.0442` n `8`; equity avg `0.0335` n `65`; fx avg `0.0047` n `5`; index avg `-0.0447` n `23`; metal avg `-0.1231` n `18`; unknown avg `-0.0159` n `375`
- 1h: commodity avg `-0.0878` n `12`; crypto_alt avg `-0.0464` n `228`; crypto_major avg `-0.0285` n `8`; equity avg `0.0941` n `65`; fx avg `0.0171` n `5`; index avg `0.0412` n `23`; metal avg `-0.1645` n `18`; unknown avg `0.2931` n `375`
- 4h: commodity avg `-0.0241` n `12`; crypto_alt avg `0.4843` n `228`; crypto_major avg `0.3372` n `8`; equity avg `0.1096` n `65`; fx avg `0.0276` n `5`; index avg `0.0813` n `23`; metal avg `-0.1479` n `18`; unknown avg `0.4513` n `375`
- 24h: commodity avg `1.7644` n `12`; crypto_alt avg `0.6071` n `228`; crypto_major avg `-1.454` n `8`; equity avg `-0.4956` n `65`; fx avg `0.2626` n `5`; index avg `-0.369` n `23`; metal avg `-0.9384` n `18`; unknown avg `-0.1442` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1349`, n `637`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1347`, n `637`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `641`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `641`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `641`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `641`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `637`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0833`, n `637`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `637`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `641`, weak_sample_signal
