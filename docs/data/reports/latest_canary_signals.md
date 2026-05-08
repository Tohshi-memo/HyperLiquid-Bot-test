# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T07:37:16.751864+00:00`
- Correlation status: `ready`
- Asset price records: `626`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0245` n `12`; crypto_alt avg `0.126` n `228`; crypto_major avg `0.1832` n `8`; equity avg `0.0862` n `65`; fx avg `-0.0092` n `5`; index avg `-0.0213` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.011` n `375`
- 1h: commodity avg `0.2337` n `12`; crypto_alt avg `0.1182` n `228`; crypto_major avg `0.1992` n `8`; equity avg `0.0575` n `65`; fx avg `-0.02` n `5`; index avg `-0.0391` n `23`; metal avg `-0.4968` n `18`; unknown avg `0.0895` n `375`
- 4h: commodity avg `-0.0551` n `12`; crypto_alt avg `-0.1077` n `228`; crypto_major avg `-0.1768` n `8`; equity avg `0.5267` n `65`; fx avg `0.1012` n `5`; index avg `0.0969` n `23`; metal avg `-0.0551` n `18`; unknown avg `-0.0003` n `355`
- 24h: commodity avg `1.2644` n `12`; crypto_alt avg `0.2369` n `228`; crypto_major avg `-2.4208` n `8`; equity avg `-1.2297` n `65`; fx avg `0.2904` n `5`; index avg `-0.7407` n `23`; metal avg `-0.5519` n `18`; unknown avg `-0.4719` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1324`, n `618`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1318`, n `618`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `622`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `622`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `622`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `622`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `618`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0812`, n `618`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `618`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `622`, weak_sample_signal
