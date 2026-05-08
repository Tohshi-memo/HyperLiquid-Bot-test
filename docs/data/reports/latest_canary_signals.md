# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T23:37:19.136278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.2219` n `228`; crypto_major avg `-0.1729` n `8`; equity avg `-0.0165` n `65`; fx avg `-0.0017` n `5`; index avg `0.0291` n `23`; metal avg `-0.0402` n `18`; unknown avg `0.1375` n `375`
- 1h: commodity avg `0.0334` n `12`; crypto_alt avg `-0.3288` n `228`; crypto_major avg `-0.3338` n `8`; equity avg `0.0057` n `65`; fx avg `0.0008` n `5`; index avg `0.0412` n `23`; metal avg `-0.1758` n `18`; unknown avg `-0.1322` n `375`
- 4h: commodity avg `-0.2883` n `12`; crypto_alt avg `0.2403` n `228`; crypto_major avg `-0.2015` n `8`; equity avg `0.6358` n `65`; fx avg `-0.039` n `5`; index avg `0.1557` n `23`; metal avg `-0.4348` n `18`; unknown avg `-0.4946` n `375`
- 24h: commodity avg `-0.8363` n `12`; crypto_alt avg `3.2352` n `228`; crypto_major avg `1.4137` n `8`; equity avg `4.0869` n `65`; fx avg `0.2255` n `5`; index avg `1.6226` n `23`; metal avg `0.7211` n `18`; unknown avg `0.9999` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
