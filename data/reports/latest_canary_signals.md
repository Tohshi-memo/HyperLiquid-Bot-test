# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T17:07:29.203268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0663` n `12`; crypto_alt avg `0.0798` n `230`; crypto_major avg `0.0803` n `8`; equity avg `-0.2232` n `98`; fx avg `-0.0036` n `6`; index avg `-0.0454` n `25`; metal avg `0.0091` n `20`; unknown avg `0.3391` n `770`
- 1h: commodity avg `0.1503` n `12`; crypto_alt avg `0.1836` n `230`; crypto_major avg `0.1155` n `8`; equity avg `-0.4339` n `98`; fx avg `-0.0043` n `6`; index avg `-0.1157` n `25`; metal avg `-0.0917` n `20`; unknown avg `0.1181` n `770`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `0.9132` n `230`; crypto_major avg `1.0758` n `8`; equity avg `-0.4153` n `98`; fx avg `-0.0884` n `6`; index avg `-0.0711` n `25`; metal avg `0.083` n `20`; unknown avg `0.2681` n `770`
- 24h: commodity avg `-0.4768` n `12`; crypto_alt avg `1.8187` n `230`; crypto_major avg `1.4657` n `8`; equity avg `0.563` n `97`; fx avg `-0.1536` n `6`; index avg `0.2059` n `25`; metal avg `0.2208` n `20`; unknown avg `0.4054` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
