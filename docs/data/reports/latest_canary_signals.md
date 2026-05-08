# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T14:22:11.987640+00:00`
- Correlation status: `ready`
- Asset price records: `653`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.167` n `12`; crypto_alt avg `0.581` n `228`; crypto_major avg `0.4515` n `8`; equity avg `0.1503` n `65`; fx avg `0.014` n `5`; index avg `-0.0142` n `23`; metal avg `-0.0353` n `18`; unknown avg `0.1614` n `375`
- 1h: commodity avg `0.3063` n `12`; crypto_alt avg `0.7681` n `228`; crypto_major avg `0.6173` n `8`; equity avg `0.9131` n `65`; fx avg `0.0076` n `5`; index avg `0.3593` n `23`; metal avg `0.0091` n `18`; unknown avg `0.3344` n `375`
- 4h: commodity avg `0.1823` n `12`; crypto_alt avg `0.7998` n `228`; crypto_major avg `0.5644` n `8`; equity avg `1.0793` n `65`; fx avg `-0.055` n `5`; index avg `0.5133` n `23`; metal avg `-0.0545` n `18`; unknown avg `0.197` n `375`
- 24h: commodity avg `2.511` n `12`; crypto_alt avg `1.7547` n `228`; crypto_major avg `-0.2871` n `8`; equity avg `0.5639` n `65`; fx avg `0.2266` n `5`; index avg `0.4374` n `23`; metal avg `-0.7762` n `18`; unknown avg `0.0176` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `645`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `645`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `649`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `645`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `649`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `649`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `645`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `649`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `649`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `649`, weak_sample_signal
