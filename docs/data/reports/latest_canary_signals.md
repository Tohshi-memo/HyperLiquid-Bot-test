# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T09:37:45.715475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0804` n `12`; crypto_alt avg `0.1801` n `229`; crypto_major avg `0.3113` n `8`; equity avg `0.2742` n `91`; fx avg `-0.0378` n `6`; index avg `0.0455` n `25`; metal avg `-0.0142` n `20`; unknown avg `0.1508` n `763`
- 1h: commodity avg `0.0294` n `12`; crypto_alt avg `-0.1144` n `229`; crypto_major avg `0.2962` n `8`; equity avg `-0.2789` n `91`; fx avg `-0.0403` n `6`; index avg `-0.0696` n `25`; metal avg `-0.3569` n `20`; unknown avg `-0.0076` n `763`
- 4h: commodity avg `0.5944` n `12`; crypto_alt avg `-1.2991` n `229`; crypto_major avg `-0.8946` n `8`; equity avg `-1.8132` n `91`; fx avg `0.0128` n `6`; index avg `-0.388` n `25`; metal avg `-1.1269` n `20`; unknown avg `-0.4859` n `743`
- 24h: commodity avg `1.3867` n `12`; crypto_alt avg `-3.7057` n `229`; crypto_major avg `-3.0093` n `8`; equity avg `-3.2486` n `91`; fx avg `-0.1639` n `6`; index avg `-0.7254` n `25`; metal avg `-1.1661` n `20`; unknown avg `-0.8399` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
