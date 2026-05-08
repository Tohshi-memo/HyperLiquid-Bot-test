# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T13:52:21.505209+00:00`
- Correlation status: `ready`
- Asset price records: `651`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `12`; crypto_alt avg `0.0495` n `228`; crypto_major avg `-0.0452` n `8`; equity avg `0.0337` n `65`; fx avg `0.0061` n `5`; index avg `0.3406` n `23`; metal avg `0.0463` n `18`; unknown avg `0.2367` n `375`
- 1h: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.1476` n `228`; crypto_major avg `-0.1736` n `8`; equity avg `0.3548` n `65`; fx avg `-0.0165` n `5`; index avg `0.2835` n `23`; metal avg `0.0017` n `18`; unknown avg `0.683` n `375`
- 4h: commodity avg `-0.2326` n `12`; crypto_alt avg `-0.0799` n `228`; crypto_major avg `-0.1924` n `8`; equity avg `0.7691` n `65`; fx avg `-0.0598` n `5`; index avg `0.5575` n `23`; metal avg `0.4678` n `18`; unknown avg `0.2787` n `375`
- 24h: commodity avg `1.6459` n `12`; crypto_alt avg `1.0676` n `228`; crypto_major avg `-0.9469` n `8`; equity avg `0.6572` n `65`; fx avg `0.2051` n `5`; index avg `0.6079` n `23`; metal avg `-0.1548` n `18`; unknown avg `-0.2912` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `643`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `643`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `647`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `647`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `647`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0931`, n `643`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `647`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `643`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `647`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `647`, weak_sample_signal
