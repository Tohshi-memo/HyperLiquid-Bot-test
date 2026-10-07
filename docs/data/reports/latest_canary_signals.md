# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T18:07:33.227290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `13`; crypto_alt avg `0.6003` n `235`; crypto_major avg `0.3123` n `8`; equity avg `0.1138` n `150`; fx avg `0.006` n `6`; index avg `0.0159` n `26`; metal avg `0.0424` n `20`; unknown avg `0.2709` n `1075`
- 1h: commodity avg `-0.2476` n `13`; crypto_alt avg `0.0514` n `235`; crypto_major avg `-0.2915` n `8`; equity avg `0.0736` n `150`; fx avg `0.0106` n `6`; index avg `0.0072` n `26`; metal avg `-0.0339` n `20`; unknown avg `0.9576` n `1075`
- 4h: commodity avg `-0.5242` n `13`; crypto_alt avg `0.3907` n `235`; crypto_major avg `-0.2063` n `8`; equity avg `0.5059` n `150`; fx avg `0.0066` n `6`; index avg `0.1596` n `26`; metal avg `0.1625` n `20`; unknown avg `-0.3208` n `1068`
- 24h: commodity avg `0.3126` n `13`; crypto_alt avg `-4.8988` n `235`; crypto_major avg `-3.8105` n `8`; equity avg `-1.7102` n `150`; fx avg `-0.1904` n `6`; index avg `-0.2663` n `26`; metal avg `-0.6249` n `20`; unknown avg `15.4417` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
