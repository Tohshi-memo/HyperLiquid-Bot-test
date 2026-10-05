# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T17:22:28.573103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.1594` n `235`; crypto_major avg `0.0808` n `8`; equity avg `0.1055` n `144`; fx avg `0.0078` n `6`; index avg `0.0162` n `26`; metal avg `0.0065` n `20`; unknown avg `40.3691` n `1079`
- 1h: commodity avg `-0.0624` n `13`; crypto_alt avg `0.2526` n `235`; crypto_major avg `0.4229` n `8`; equity avg `0.0977` n `144`; fx avg `0.0007` n `6`; index avg `0.0367` n `26`; metal avg `0.0114` n `20`; unknown avg `0.0692` n `1077`
- 4h: commodity avg `0.0237` n `13`; crypto_alt avg `-1.0593` n `235`; crypto_major avg `-0.603` n `8`; equity avg `0.1368` n `144`; fx avg `-0.038` n `6`; index avg `0.1358` n `26`; metal avg `-0.1541` n `20`; unknown avg `0.6007` n `989`
- 24h: commodity avg `-0.3139` n `13`; crypto_alt avg `-0.0487` n `235`; crypto_major avg `0.0931` n `8`; equity avg `0.234` n `144`; fx avg `-0.1047` n `6`; index avg `0.1146` n `26`; metal avg `0.1216` n `20`; unknown avg `-0.2703` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
