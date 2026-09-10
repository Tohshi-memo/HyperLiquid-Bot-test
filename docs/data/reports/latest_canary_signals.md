# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T13:22:30.118304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2354` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4403` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1425` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `-0.0022` n `233`; crypto_major avg `-0.0511` n `8`; equity avg `-0.093` n `134`; fx avg `0.0042` n `6`; index avg `-0.0315` n `26`; metal avg `0.0124` n `20`; unknown avg `470.9297` n `797`
- 1h: commodity avg `0.1416` n `12`; crypto_alt avg `-0.8425` n `233`; crypto_major avg `-1.3064` n `8`; equity avg `-0.8672` n `134`; fx avg `-0.0318` n `6`; index avg `-0.1639` n `26`; metal avg `-0.1579` n `20`; unknown avg `0.7031` n `789`
- 4h: commodity avg `0.5017` n `12`; crypto_alt avg `-1.3299` n `233`; crypto_major avg `-1.7337` n `8`; equity avg `-1.5661` n `134`; fx avg `0.0107` n `6`; index avg `-0.2934` n `26`; metal avg `-0.769` n `20`; unknown avg `0.2405` n `789`
- 24h: commodity avg `0.4742` n `12`; crypto_alt avg `-5.6756` n `233`; crypto_major avg `-4.7768` n `8`; equity avg `-2.4825` n `134`; fx avg `0.1017` n `6`; index avg `-0.3205` n `26`; metal avg `-1.0028` n `20`; unknown avg `-1.2384` n `669`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
