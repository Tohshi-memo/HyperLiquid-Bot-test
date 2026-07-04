# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T10:07:25.719313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.0783` n `229`; crypto_major avg `0.0422` n `8`; equity avg `-0.0107` n `88`; fx avg `-0.0057` n `6`; index avg `0.0001` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0092` n `765`
- 1h: commodity avg `0.0885` n `12`; crypto_alt avg `-0.1261` n `229`; crypto_major avg `-0.0657` n `8`; equity avg `0.0203` n `88`; fx avg `0.0011` n `6`; index avg `0.0047` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.195` n `765`
- 4h: commodity avg `0.0817` n `12`; crypto_alt avg `-0.6171` n `229`; crypto_major avg `-0.5324` n `8`; equity avg `-0.0303` n `88`; fx avg `-0.0191` n `6`; index avg `0.0101` n `25`; metal avg `0.0159` n `20`; unknown avg `0.4704` n `765`
- 24h: commodity avg `0.0567` n `12`; crypto_alt avg `1.0222` n `229`; crypto_major avg `2.044` n `8`; equity avg `0.3088` n `88`; fx avg `-0.0645` n `6`; index avg `-0.017` n `25`; metal avg `-0.1284` n `20`; unknown avg `5.4937` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
