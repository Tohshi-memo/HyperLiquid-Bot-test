# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T21:52:15.952092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0914` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0818` n `12`; crypto_alt avg `-0.0143` n `228`; crypto_major avg `0.0292` n `8`; equity avg `-0.0367` n `67`; fx avg `0.0023` n `6`; index avg `0.023` n `23`; metal avg `-0.0686` n `18`; unknown avg `-0.0621` n `396`
- 1h: commodity avg `0.0387` n `12`; crypto_alt avg `-0.9783` n `228`; crypto_major avg `-0.5756` n `8`; equity avg `-0.1877` n `67`; fx avg `0.0059` n `6`; index avg `-0.0102` n `23`; metal avg `-0.2754` n `18`; unknown avg `0.1622` n `396`
- 4h: commodity avg `0.1429` n `12`; crypto_alt avg `-1.6714` n `228`; crypto_major avg `-1.177` n `8`; equity avg `-0.1476` n `67`; fx avg `0.0443` n `6`; index avg `-0.0856` n `23`; metal avg `-0.4455` n `18`; unknown avg `-0.5737` n `396`
- 24h: commodity avg `1.316` n `12`; crypto_alt avg `-3.0227` n `228`; crypto_major avg `-0.3146` n `8`; equity avg `0.3455` n `67`; fx avg `0.1045` n `6`; index avg `-0.07` n `23`; metal avg `-0.3681` n `18`; unknown avg `0.0596` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
