# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T09:22:16.083374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1529` n `12`; crypto_alt avg `0.1263` n `228`; crypto_major avg `0.1341` n `8`; equity avg `-0.0161` n `66`; fx avg `0.0173` n `6`; index avg `-0.0148` n `23`; metal avg `-0.0659` n `18`; unknown avg `-0.2958` n `384`
- 1h: commodity avg `-0.2404` n `12`; crypto_alt avg `0.1982` n `228`; crypto_major avg `0.1973` n `8`; equity avg `0.0843` n `66`; fx avg `-0.017` n `6`; index avg `0.082` n `23`; metal avg `0.022` n `18`; unknown avg `0.109` n `384`
- 4h: commodity avg `-0.5168` n `12`; crypto_alt avg `0.5246` n `228`; crypto_major avg `0.497` n `8`; equity avg `0.7484` n `66`; fx avg `-0.0693` n `6`; index avg `0.4236` n `23`; metal avg `0.7232` n `18`; unknown avg `0.0059` n `374`
- 24h: commodity avg `-0.1848` n `12`; crypto_alt avg `0.6195` n `228`; crypto_major avg `0.2946` n `8`; equity avg `1.0136` n `66`; fx avg `-0.1285` n `6`; index avg `0.0256` n `23`; metal avg `-0.9472` n `18`; unknown avg `0.6694` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
