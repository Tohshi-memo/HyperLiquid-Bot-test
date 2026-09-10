# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T12:52:32.451565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1436` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3856` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2306` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0576` n `12`; crypto_alt avg `-0.5926` n `233`; crypto_major avg `-0.7666` n `8`; equity avg `-0.2369` n `134`; fx avg `-0.0281` n `6`; index avg `-0.0276` n `26`; metal avg `0.0874` n `20`; unknown avg `34.2558` n `797`
- 1h: commodity avg `0.3559` n `12`; crypto_alt avg `-1.1587` n `233`; crypto_major avg `-1.4152` n `8`; equity avg `-1.0822` n `134`; fx avg `-0.0025` n `6`; index avg `-0.1846` n `26`; metal avg `-0.311` n `20`; unknown avg `0.448` n `789`
- 4h: commodity avg `0.4816` n `12`; crypto_alt avg `-1.3558` n `233`; crypto_major avg `-1.662` n `8`; equity avg `-1.469` n `134`; fx avg `0.0043` n `6`; index avg `-0.2764` n `26`; metal avg `-0.8131` n `20`; unknown avg `0.2901` n `789`
- 24h: commodity avg `0.4396` n `12`; crypto_alt avg `-5.8156` n `233`; crypto_major avg `-4.8551` n `8`; equity avg `-2.2455` n `134`; fx avg `0.1019` n `6`; index avg `-0.2777` n `26`; metal avg `-0.7272` n `20`; unknown avg `-1.0358` n `669`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
