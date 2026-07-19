# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T20:52:24.159830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `0.0376` n `8`; equity avg `0.0084` n `96`; fx avg `-0.0038` n `6`; index avg `0.0073` n `25`; metal avg `-0.0209` n `20`; unknown avg `0.0126` n `771`
- 1h: commodity avg `0.0569` n `12`; crypto_alt avg `0.1708` n `230`; crypto_major avg `0.1927` n `8`; equity avg `0.0626` n `96`; fx avg `0.0592` n `6`; index avg `0.0203` n `25`; metal avg `-0.0315` n `20`; unknown avg `0.0349` n `771`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0724` n `230`; crypto_major avg `0.159` n `8`; equity avg `0.1565` n `96`; fx avg `0.0645` n `6`; index avg `0.058` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.004` n `770`
- 24h: commodity avg `0.0215` n `12`; crypto_alt avg `0.0732` n `230`; crypto_major avg `0.4454` n `8`; equity avg `0.4392` n `96`; fx avg `0.1261` n `6`; index avg `-0.0181` n `25`; metal avg `-0.007` n `20`; unknown avg `0.0447` n `752`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1545`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1471`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1349`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1237`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1055`, n `666`, weak_sample_signal
