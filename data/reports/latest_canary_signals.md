# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T22:52:29.024513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1042` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4536` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0119` n `13`; crypto_alt avg `-0.0038` n `239`; crypto_major avg `-0.0586` n `8`; equity avg `0.0311` n `166`; fx avg `-0.0025` n `6`; index avg `0.0037` n `27`; metal avg `0.008` n `20`; unknown avg `1.5649` n `1266`
- 1h: commodity avg `-0.0268` n `13`; crypto_alt avg `-0.7134` n `239`; crypto_major avg `-0.4753` n `8`; equity avg `0.4057` n `166`; fx avg `0.017` n `6`; index avg `0.0526` n `27`; metal avg `0.0472` n `20`; unknown avg `207.2652` n `1258`
- 4h: commodity avg `-0.1381` n `13`; crypto_alt avg `-2.0096` n `239`; crypto_major avg `-1.3582` n `8`; equity avg `0.746` n `166`; fx avg `0.012` n `6`; index avg `0.0954` n `27`; metal avg `-0.0648` n `20`; unknown avg `206.0065` n `1222`
- 24h: commodity avg `-1.4153` n `13`; crypto_alt avg `0.481` n `239`; crypto_major avg `0.813` n `8`; equity avg `6.278` n `166`; fx avg `-0.1665` n `6`; index avg `0.6435` n `27`; metal avg `0.6296` n `20`; unknown avg `3.768` n `1048`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
