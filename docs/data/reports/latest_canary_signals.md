# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T22:33:45.245811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.0784` n `230`; crypto_major avg `-0.1222` n `8`; equity avg `-0.0161` n `114`; fx avg `-0.0047` n `6`; index avg `-0.0004` n `25`; metal avg `0.0372` n `20`; unknown avg `-0.0981` n `791`
- 1h: commodity avg `-0.0927` n `12`; crypto_alt avg `-0.4032` n `230`; crypto_major avg `-0.4213` n `8`; equity avg `-0.0348` n `114`; fx avg `-0.0098` n `6`; index avg `0.0275` n `25`; metal avg `0.0273` n `20`; unknown avg `-0.0575` n `791`
- 4h: commodity avg `-0.0782` n `12`; crypto_alt avg `-0.7986` n `230`; crypto_major avg `-0.5698` n `8`; equity avg `0.0103` n `114`; fx avg `-0.0045` n `6`; index avg `0.0392` n `25`; metal avg `-0.0116` n `20`; unknown avg `-0.0137` n `791`
- 24h: commodity avg `-0.017` n `12`; crypto_alt avg `-1.0631` n `230`; crypto_major avg `-0.6298` n `8`; equity avg `0.2534` n `114`; fx avg `-0.01` n `6`; index avg `0.0634` n `25`; metal avg `0.0346` n `20`; unknown avg `-0.0148` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
