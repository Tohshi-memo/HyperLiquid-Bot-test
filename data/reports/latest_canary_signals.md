# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T03:08:04.267478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `0.1668` n `234`; crypto_major avg `0.0211` n `8`; equity avg `-0.013` n `140`; fx avg `-0.0214` n `6`; index avg `0.0055` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.8336` n `943`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.9619` n `234`; crypto_major avg `0.6081` n `8`; equity avg `0.0601` n `140`; fx avg `-0.0195` n `6`; index avg `0.0019` n `26`; metal avg `-0.0171` n `20`; unknown avg `0.6264` n `943`
- 4h: commodity avg `0.0084` n `12`; crypto_alt avg `0.2749` n `234`; crypto_major avg `0.1241` n `8`; equity avg `-0.3452` n `140`; fx avg `-0.0689` n `6`; index avg `-0.0995` n `26`; metal avg `-0.2927` n `20`; unknown avg `0.969` n `937`
- 24h: commodity avg `-0.0512` n `12`; crypto_alt avg `3.7419` n `234`; crypto_major avg `2.1862` n `8`; equity avg `0.2858` n `140`; fx avg `-0.2035` n `6`; index avg `0.001` n `26`; metal avg `0.0766` n `20`; unknown avg `1.4466` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
