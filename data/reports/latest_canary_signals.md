# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T03:52:24.964847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1963` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `-0.0381` n `231`; crypto_major avg `-0.0707` n `8`; equity avg `-0.0708` n `127`; fx avg `-0.0129` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0233` n `20`; unknown avg `-0.0535` n `792`
- 1h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.197` n `231`; crypto_major avg `0.1457` n `8`; equity avg `-0.007` n `127`; fx avg `-0.0333` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0223` n `20`; unknown avg `-0.0315` n `792`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `-1.3304` n `231`; crypto_major avg `-1.1176` n `8`; equity avg `0.1254` n `127`; fx avg `-0.0631` n `6`; index avg `0.0787` n `26`; metal avg `-0.0855` n `20`; unknown avg `0.0728` n `792`
- 24h: commodity avg `0.29` n `12`; crypto_alt avg `0.3594` n `231`; crypto_major avg `1.7927` n `8`; equity avg `-0.0713` n `127`; fx avg `-0.04` n `6`; index avg `0.0351` n `26`; metal avg `-0.1224` n `20`; unknown avg `0.6061` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
